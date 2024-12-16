rm(list = ls())
library(survival)
library(rms)

my_data <- read.csv("F:\\yunnan_predict_others_riskscores\\yunnan_predict_ZJH_riskscores_with_HazardGroup.csv")

dd <- datadist(my_data)
options(datadist = "dd")

# 2 year                       730 days / 24 months      
coxfit1 <- cph(Surv(survival_time, event_status) ~ hazard_score + Age + tumor_size_count + BCLC,
               data = my_data, x=T,y=T,surv = T,
               time.inc = 730) 

cal1 <- calibrate(coxfit1,cmethod="KM",method="boot", m=50, u=730, B=500)
print(cal1)
plot(cal1,
     lwd = 2,
     lty = 0, 
     errbar.col = c("#27ae60"), 
     xlim = c(0, 1), ylim = c(0, 1), 
     xlab = "Predicted Probability",ylab = "Observed Probability",
     cex.lab=1, cex.axis=1, cex.main=1.2, cex.sub=0.1) 
lines(cal1[,c('mean.predicted',"KM")],
      type = 'b', 
      lwd = 3, 
      pch = 16, 
      col = "#1f618d") 
lines(cal1[,c('mean.predicted',"KM.corrected")],
      type = 'b', 
      lwd = 3, 
      pch = 16, 
      col = "#e74c3c") 
box(lwd = 2) 
abline(0,1,lty = 3,
       lwd = 2, 
       col = "grey70" 
)





