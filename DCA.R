
# install.packages("remotes")
# remotes::install_github('yikeshu0611/ggDCA')

rm(list = ls())
library(survival)
library(ggDCA)
library(rmda)
my_data <- read.csv("F:\\yunnan_predict_others_riskscores\\yunnan_predict_ZJH_riskscores_with_HazardGroup.csv")
cutpoint <-  0.15337              
# my_data$hazard_group <- ifelse(my_data$hazard_score <= cutpoint, 0, 1)
 
MINF <- coxph(Surv(survival_time,event_status)~ hazard_score, data=my_data)
Full_model <- coxph(Surv(survival_time,event_status)~ hazard_score +  Age + tumor_size_count + BCLC, data=my_data)
Clinical_model <- coxph(Surv(survival_time,event_status)~  Age + tumor_size_count + BCLC, data=my_data)

# Plot DCA         730 days / 24 months
plot1 <- dca(Full_model, Clinical_model, MINF,  times=730,
             model.names =c('Full model','Clinicopathological model', 'MINF'))
summary(plot1)

ggplot(plot1) +
  theme(legend.position =  c(0.7, 0.85),
        legend.text = element_text(size = 15))

