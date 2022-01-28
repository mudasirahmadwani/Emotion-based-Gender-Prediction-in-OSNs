install.packages(rpart)

library(rpart)

#mydata_dt=read.csv(file.choose())
mydata_dt=read_delim(file.choose(),";", escape_double = FALSE, trim_ws = TRUE)
mydata_dt=mydata_dt[-1]

set.seed(3433)

trainIndex <- createDataPartition(mydata_dt$Gender, p=0.7, list=FALSE)
data_train <- mydata_dt[ trainIndex,]
data_test <- mydata_dt[-trainIndex,]
dim(data_train);
dim(data_test);

# fit model
fit <- rpart(Gender~., data=data_train)
# summarize the fit
summary(fit)
# make predictions
predictions <- predict(fit,data_test, type="class")
# summarize accuracy
table(predictions, data_test$Gender)
#y_test <- data_test[,11]
y_test <- as.factor(data_test$Gender)

confusionMatrix(predictions, y_test)




################################  ROC  ##############################################

#--------------ROC Decision Tree ############
gc_prob_dt <- predict(svm_Radial, newdata = data_test, type = "prob")
gc_prob_dt
gc_pROC <- roc(response = data_test$Gender, predictor = gc_prob_dt[, "M"],smooth = TRUE)
plot(gc_pROC,col="#02c3c1", lwd=2, main=" ", xlab="True Positive Rate", ylab="False Positive Rate ",
     print.auc=TRUE,
     auc.polygon=TRUE)

####################### RANDOM FOREST ########################################
