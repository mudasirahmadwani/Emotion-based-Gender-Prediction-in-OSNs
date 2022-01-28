install.packages("caret")
install.packages("klaR")
install.packages("e1071")

# load the libraries
library(caret)
library(klaR)
library(e1071)
library(xlsReadWrite)
head(mydata)

#mydata=read_delim("DATA-mudasir/emotion_based_genderPrediction(commaSep).csv",";", escape_double = FALSE, trim_ws = TRUE)
#mydata=read_delim(file.choose(),";", escape_double = FALSE, trim_ws = TRUE)

mydata=read.csv(file.choose())

mydata=mydata[-1]

# define an 70%/30% train/test split of the dataset

set.seed(2244)
split=0.70
mydata=as.vector(mydata)
trainIndex <- createDataPartition(mydata$gender, p=split, list=FALSE)
data_train <- mydata[ trainIndex,]
data_test <- mydata[-trainIndex,]
# train a naive bayes model
str(data_train$gender)
model <- NaiveBayes(gender~., data=data_train)

length(mydata$Gender)
length(data_train$fear)

dim(mydata)
str(mydata)
# make predictions
x_test <- data_test[,1:11]

y_test <- data_test[,12]
predictions <- predict(model, data_test)

# summarize results
confusionMatrix(predictions$class, y_test)


####################### NB ROC####################
PredictionNBModel <- NaiveBayes(gender~., data=data_train)
PredictionsWithProbs=predict(PredictionNBModel,data_test, type = 'prob')
#PredictionsWithProbs$posterior
auc=auc(data_test$gender,PredictionsWithProbs$posterior[,2])
NB_ROC=roc(data_test$gender,PredictionsWithProbs$posterior[,2],smooth = TRUE)
plot(NB_ROC,col="blue", lwd=3, main="ROC (Naive Bayes) ", xlab="True Positive Rate", ylab="False Positive Rate ")
NB_ROC$auc


#############################################################################################




# load the library
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="boot", number=100)
# train the model
model <- train(label~., data=mydata, trControl=train_control, method="nb")
# summarize results
print(model)


library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="repeatedcv", number=10, repeats=3)
# train the model
model <- train(label~., data=mydata, trControl=train_control, method="nb")
# summarize results
print(model)




# load the library
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="LOOCV")
# train the model
model <- train(Species~., data=iris, trControl=train_control, method="nb")
# summarize results
print(model)




# load the library
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="LOOCV")
# train the model
model <- train(label~., data=mydata, trControl=train_control, method="nb")
# summarize results
print(model)
