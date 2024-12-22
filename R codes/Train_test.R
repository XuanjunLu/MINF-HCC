library(survival)
# library(rms)
rm(list = ls())

# train data
train_data <- read.csv("F:\\FLocK_Morph_Haralick_matrix_yunnan_with_duration_event.csv")
col_to_remove_train = c('patient_id', 'patient_id_median_x', 'patient_id_std_x',
                        'patient_id_kurtosis_x', 'patient_id_skew_x', 
                        'patient_id_median_y', 'patient_id_std_y', 
                        'patient_id_kurtosis_y', 'patient_id_skew_y',
                        'event_status', 'survival_time')

event_status_train <- train_data$event_status
survival_time_train <- train_data$survival_time

data_value_train <- train_data[, !(names(train_data) %in% col_to_remove_train)]
# Z-scores 
data_value_scores_train <- scale(data_value_train)
# NA cols
na_columns_train <- colSums(is.na(data_value_scores_train)) == nrow(data_value_scores_train)
# remove NA cols
data_value_scores_train <- data_value_scores_train[, !na_columns_train]

# concat
data_matrix_train <- cbind(event_status_train,survival_time_train,data_value_scores_train)
data_matrix_train <- as.data.frame(data_matrix_train)

# test data
test_data <- read.csv("F:\\FLocK_Morph_Haralick_matrix_ZZH_with_duration_event.csv")
col_to_remove_test = c('patient_id', 'patient_id_median_x', 'patient_id_std_x',
                       'patient_id_kurtosis_x', 'patient_id_skew_x', 
                       'patient_id_median_y', 'patient_id_std_y', 
                       'patient_id_kurtosis_y', 'patient_id_skew_y',
                       'event_status', 'survival_time')

event_status_test <- test_data$event_status
survival_time_test <- test_data$survival_time

data_value_test <- test_data[, !(names(test_data) %in% col_to_remove_test)]

# Z-scores 
data_value_scores_test <- scale(data_value_test)
na_columns_test <- colSums(is.na(data_value_scores_test)) == nrow(data_value_scores_test)
data_value_scores_test <- data_value_scores_test[, !na_columns_test]

data_matrix_test <- cbind(event_status_test,survival_time_test,data_value_scores_test)
data_matrix_test <- as.data.frame(data_matrix_test)



################################################################################
# top 15 discriminative features
cox_model <- coxph(Surv(survival_time_train, event_status_train) ~  Shape_Standard_Deviation_LongorShort_Distance_Ratio_average +
                     Shape_Median_Perimeter_Ratio_median +
                     Shape_Min_or_Max_Standard_Deviation_of_Distance_median +
                     GLCM_kurtosis_contrast_inverse_moment_median +
                     Shape_Min_or_Max_Area_Ratio_std +
                     Shape_Standard_Deviation_Variance_of_Distance_kurtosis +
                     GLCM_mean_information_measure1_kurtosis +
                     Shape_Median_Perimeter_Ratio_skew +
                     GLCM_std_intensity_ave_skew +
                     FLocK_OutSpatialClusterRrMean10_average +
                     FLocK_OutPolygonFlockOtherAttrKurtosis_median +
                     FLocK_OutSizeFlockNucDensityOverSizeSkewness_std +
                     FLocK_OutSpatialClusterDelaunayAreaMinMax_kurtosis +
                     FLocK_OutSpatialClusterRrStd20_kurtosis +
                     FLocK_OutSpatialClusterRrStd50_skew,
                     data = data_matrix_train)

summary(cox_model)

# AIC
aic_value <- AIC(cox_model)
print(paste("AIC:", aic_value))

hazard_score <- predict(cox_model, newdata = data_matrix_test, type = "lp")


# concat
hazard_score_ev_sur <- cbind(hazard_score, survival_time_test, event_status_test)
# rename
colnames(hazard_score_ev_sur) <- c("hazard_score", "survival_time", "event_status")
# write.csv(hazard_score_ev_sur, file = "F:\\yunnan_predict_ZZH_riskscores.csv", row.names = FALSE)
# C-index
concordance <- survConcordance(Surv(survival_time_test, event_status_test) ~ hazard_score, data = data_matrix_test)
c_index <- concordance$concordance
print(c_index)




