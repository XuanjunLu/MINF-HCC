
library(car)
library(survival)
library(glmnet)
# library(survC1)
library(MASS)

rm(list = ls())
best_aic <- Inf
best_model <- NULL

data <- read.csv("F:\\FLocK_Morph_Haralick_matrix_yunnan_with_duration_event.csv")
col_to_remove = c('patient_id', 'patient_id_median_x', 'patient_id_std_x',
                  'patient_id_kurtosis_x', 'patient_id_skew_x', 
                  'patient_id_median_y', 'patient_id_std_y', 
                  'patient_id_kurtosis_y', 'patient_id_skew_y',
                  'event_status', 'survival_time')
event_status <- data$event_status
survival_time <- data$survival_time
data_value <- data[, !(names(data) %in% col_to_remove)]


# Z-scores
data_value_scores <- scale(data_value)
na_columns <- colSums(is.na(data_value_scores)) == nrow(data_value_scores)
data_value_scores <- data_value_scores[, !na_columns]

# concat event_status'，'survival_time', Z-scores data
data_matrix <- cbind(event_status,survival_time,data_value_scores)
data_matrix <- as.data.frame(data_matrix)



#####--------------------------Univariable analysis------------------------#####

selected_features <- c()
for (feature in colnames(data_matrix)[-c(1,2)]) {
  formula <- as.formula(paste("Surv(survival_time, event_status) ~", feature))
  model_univ <- coxph(formula, data = data_matrix)
  
  summary_model <- summary(model_univ)
  
  p_value <- summary_model$coefficients[1, 5]  # p value
  
  if (p_value <= 0.05) {
    selected_features <- c(selected_features, feature)
  }
}

print(length(selected_features))

# filtered data
data_matrix_filtered <- data_matrix[, c('survival_time', 'event_status', selected_features)]




n = 0
for (i in 1:100) {
  n = n + 1
  print(n)
  
  ####---------------------lasso-cox feature selection---------------------####
  
  x <- as.matrix(data_matrix_filtered[, selected_features])
  y <- with(data_matrix_filtered, Surv(survival_time, event_status))
  
  # glmnet Lasso-Cox 
  fit <- glmnet(x, y, family = "cox", alpha=1)
  cv_fit <- cv.glmnet(x, y, family = "cox", alpha=1,nfolds=10)
  # plot(cv_fit)
  lambda_min <- cv_fit$lambda.min
  power_features <- coef(cv_fit, s = "lambda.min")
  
  # print(power_features)
  feature_index <- which(as.numeric(power_features) != 0)
  
  # features and coefficients
  feature_coef <- as.numeric(power_features)[feature_index]
  feature_name <- rownames(power_features)[feature_index]
  len_feature_name <- paste("The number of features in lasso-cox：", length(feature_name))
  print(length(feature_name))
  # print(feature_name)
  
  
  
  
  ####-------------------------------------AIC-based stepwise regression-------------------------------------####
  
  final_model <- coxph(Surv(survival_time, event_status) ~ ., 
                       data = data_matrix_filtered[, c('survival_time', 
                                                       'event_status', feature_name)])
  step_model <- stepAIC(final_model, direction = "both", trace = 0) 
  
  # smallest AIC model
  current_aic <- AIC(step_model)
  if (current_aic < best_aic) {
    best_aic <- current_aic
    best_model <- step_model
  }
}
  

summary_best_model <- summary(best_model)
print(summary_best_model)
print(best_aic)



