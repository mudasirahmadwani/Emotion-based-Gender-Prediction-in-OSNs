alldata <- read.csv("D:\\Desktop\\Mudasir\\Gender Prediction (comsnets)\\combined(in clause)-with Emotionvariance_and_Platform_info.csv", sep = ",")

fbData = alldata[alldata$platform==1,]
mydata_rf = fbData[,2:14]
library(randomForest)
library(caret)
library(ROCR)
library(pROC)
library(e1071)
library(gplots)
library(klaR)

mydata=read.csv(file.choose())
mydata_rf = mydata_rf[-1]
mydata_rf$gender = as.factor(mydata_rf$gender)

mydata_rf= na.omit(mydata_rf)
set.seed(80)
trainIndex <- createDataPartition(mydata_rf$gender, p=0.9, list=FALSE)
dim(trainIndex)
data_train <- mydata_rf[trainIndex,]
data_test <- mydata_rf[-trainIndex,]

data_test$gender
data_test

# train a random forest model
control <- trainControl(method="repeatedcv", number=10, repeats=3, search="random")
output.forest <- randomForest(gender~.,data = data_train,mtry=9,trControl=control)
rf_prediction_test <- (predict(output.forest,data_test))

# train a svm model
trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3,classProbs = TRUE,
                       summaryFunction = twoClassSummary)
svm_Radial <- train(gender ~., data = data_train, method = "svmRadial",
                    trControl=trctrl,
                    preProcess = c("center", "scale"),
                    tuneLength = 5)
test_pred_Radial <- (predict(svm_Radial, data_test))


# train a naive bayes model
model <- NaiveBayes(gender~., data=data_train)
naive_predictions <- (predict(model, data_test))
naive_predictions = (naive_predictions$class)

testResults = data.frame(cbind(rf_prediction_test,test_pred_Radial,naive_predictions,data_test$gender))
#write.csv(testResults, file = "D:\\Desktop\\Mudasir\\Gender Prediction (comsnets)\\majority_voting_predction.csv")
write.csv(testResults, file = "C:\\Users\\mudasirw\\Desktop\\RESEARCH @N T N U -JULY 2019\\GENDER PREDICTION\\majority_voting_predction_actual_fb_new1.csv")


#---------------------------Accuracy after majority Voting -------------------------------
mv=read.csv(file.choose())

str(mv)

mv$Column2=as.factor(mv$Column2)
mv$V4=as.factor(mv$V4)

#mv$rf_prediction_test=as.factor(mv$rf_prediction_test)
#mv=as.factor(mv)

confusionMatrix(mv$Column2, mv$V4)
levels(mv$majority_vote)
levels(mv$actaul_class)

