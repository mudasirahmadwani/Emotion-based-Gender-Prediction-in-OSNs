install.packages("pROC")
install.packages("readr")
library(readr)
library(caret)
library(ROCR)
library(pROC)
library(e1071)

mydata=read.csv(file.choose())
#mydata=read_delim(file.choose(),";", escape_double = FALSE, trim_ws = TRUE)

mydata = mydata[-1]
head(mydata)
dim(mydata)
anyNA(mydata)
mydata=na.omit(mydata)
anyNA(mydata)
dim(mydata)

#set.seed(3231)
set.seed(3242)
intrain <- createDataPartition(y = mydata$gender, p= 0.8, list = FALSE)
training <- mydata[intrain,]
testing <- mydata[-intrain,]

dim(training); dim(testing);

trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3,classProbs = TRUE,
                       summaryFunction = twoClassSummary)

#=========================SVM Radial (Non-Linear)======================================
#==========================Training SVM Radial

#set.seed(2322)
#set.seed(3231)
svm_Radial <- train(gender ~., data = training, method = "svmRadial",
                    trControl=trctrl,
                    preProcess = c("center", "scale"),
                    tuneLength = 5)
#svm_Radial
#plot(svm_Radial)

#Testing=======================================================================
test_pred_Radial <- predict(svm_Radial, newdata = testing)

#testing$gender <- as.factor(testing$gender)
confusionMatrix(test_pred_Radial, testing$gender)

### Tuning SVM Radial==========================================================

grid_radial <- expand.grid(sigma = c(0.75,0.9,2,3,4,5),
                           C = c(0.05, 0.1, 0.25, 0.5, 0.75,
                                 1, 1.5, 2,5, 6, 7, 8, 9, 10, 15, 20, 25,30))


#Training svm Radial after tuning ================================================== 


svm_Radial <- train(gender ~., data = training, method = "svmRadial",
                    trControl=trctrl,
                    tuneGrid=grid_radial,
                    preProcess = c("center", "scale"),
                    tuneLength = 10)
#svm_Radial
plot(svm_Radial)

# Testing SVM Radial after Tuning ==============================================  

test_pred_Radial <- predict(svm_Radial, newdata = testing)
confusionMatrix(test_pred_Radial, testing$gender)

#==============================plot ROC=========================

svm_Radial=na.omit(svm_Radial)
gc_prob <- predict(svm_Radial, newdata = testing, type = "prob")
gc_prob
gc_pROC <- roc(response = testing$gender, predictor = gc_prob[, "M"],smooth = TRUE)
plot(gc_pROC,col="#02c3c1", lwd=2, main=" ", xlab="True Positive Rate", ylab="False Positive Rate ",
     print.auc=TRUE,
     auc.polygon=TRUE)

gc_pROC$auc

### j48 ROC #####
plot(gcRoc, col="blue", add = TRUE,lwd=3)
plot(NB_ROC,col="brown", add = TRUE,lwd=3)   



