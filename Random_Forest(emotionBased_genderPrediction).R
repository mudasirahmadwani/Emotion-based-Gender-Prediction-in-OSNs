install.packages("e1071")
install.packages("ROCR")
install.packages("randomForest")
require(randomForest)
library(randomForest)
library(e1071)
library(caret)
library(ROCR)

mydata_rf = read.csv(file.choose())

#mydata_rf=read_delim(file.choose(),";", escape_double = FALSE, trim_ws = TRUE)
mydata_rf = mydata_rf[-1]   # Removing first coloumn (profile link)
#mydata_rf[12]
#dim(mydata_rf)
#mydata_rf=as.factor(mydata_rf)
mydata_rf= na.omit(mydata_rf)
dim(mydata_rf)
#Partitioning the data into training and validation data
#------------------------------------------------------------------------

set.seed(3242)
trainIndex <- createDataPartition(mydata_rf$gender, p=0.8, list=FALSE)
dim(trainIndex)
data_train <- mydata_rf[ trainIndex,]
data_test <- mydata_rf[-trainIndex,]
#names(data_test)
#names(data_train)
#summary(mydata_rf$gender)
#x=length(data_test)

#fb_data=data_test[data_test$platform==1,]
#twtr_data=data_test[data_test$platform==2,]
#-------------------------------------------------traning randomForest model---------------------------------
control <- trainControl(method="repeatedcv", number=10, repeats=2, search="random")
output.forest <- randomForest(gender~.,data = data_train,mtry=9,trControl=control)

#-----------------------prediction/ testing on other data-sets----------------------------------
#t_testdata=read.csv(file.choose())
#t_testdata= t_testdata[-1]
#prediction_test <- predict(output.forest,t_testdata)
#t_testdata$gender=as.factor(t_testdata$gender)
#confusionMatrix(data=prediction_test,reference=t_testdata$gender)
# -------------------------------prediction on Test sample ----------------------------
prediction_test <- predict(output.forest,data_test)
#prediction_test[,1]
#data_test$gender=as.factor(data_test$gender)

#varImpPlot(output.forest, main ='Feature importance',col="blue")
#varImp(output.forest, main ='Feature importance')
#-----------------------------------------confusionMatrix---------------------------------
confusionMatrix(data=prediction_test,reference=data_test$gender)

#-------------------- ROC (Random Forest) ---------------------------
gc_prob_rf <- predict(output.forest, newdata = data_test, type = "prob")
gc_prob_rf
length(data_test$gender)
length(predictor)
gc_pROC_rf <- roc(response = data_test$gender, predictor = gc_prob_rf[, "Male"],smooth = TRUE)
plot(gc_pROC_rf,col="#02c3c1", lwd=3, main=" ", xlab="True Positive Rate", ylab="False Positive Rate ",
     print.auc=TRUE,
     auc.polygon=TRUE)

gc_pROC_rf$auc





