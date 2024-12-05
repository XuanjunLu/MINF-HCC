
rm(list = ls())
observed <- matrix(c(94, 42, 1, 66, 13, 0), nrow = 3, ncol = 2)
print(observed)

####################### Pearson’s chi-square test #############################
chisq_test <- chisq.test(observed, correct = FALSE)  # FALSE     
chisq_test$expected  
chisq_test$p.value
# print(summary(chisq_test))


#############################Fisher’s exact test###############################
fisher_test_result <- fisher.test(observed)
fisher_test_result


################################ Mann-Whitney U test ##########################
rm(list = ls())
data1 <- read.csv("F:\\FLocK_Shape_GLCM_matrix_yunnan_with_duration_event_addcli.csv")
data2 <- read.csv("F:\\FLocK_Shape_GLCM_matrix_ZJH_with_duration_event_addcli.csv")

group1 <- data1$ALBI_score
group2 <- data2$ALBI_score

test_result <- wilcox.test(group1, group2, exact = TRUE)
cat("P-value:", test_result$p.value, "\n")
