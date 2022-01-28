install.packages("caret")
install.packages("klaR")
install.packages("e1071")

# load the libraries
library(caret)
library(klaR)
library(e1071)
#mydata=read_delim("DATA-mudasir/emotion_based_genderPrediction(commaSep).csv",";", escape_double = FALSE, trim_ws = TRUE)
mydata_nb=read.csv(file.choose())

mydata_nb=mydata_nb[-1]
dim(mydata_nb)

# define an 70%/30% train/test split of the dataset
mydata_nb$gender=as.factor(mydata_nb$gender)
set.seed(3242)
split=0.70
mydata_nb=as.vector(mydata_nb)
trainIndex <- createDataPartition(mydata_nb$gender, p=split, list=FALSE)
data_train <- mydata_nb[ trainIndex,]
data_test <- mydata_nb[-trainIndex,]
dim(data_train)
dim(data_test)


mydata_nb$email_id=as.character(mydata_nb$email_id)
# train a naive bayes model
model <- NaiveBayes(gender~., data=data_train)
str(mydata)
# make predictions
x_test <- data_test[,1:11]
y_test <- data_test[,12]


dim(x_test)
dim(y_test)
predictions <- predict(model, data_test)

# Some necessary checks 
#levels(predictions$class)
#levels(y_test)
#table(predictions$class)
#table(y_test)
#str(predictions$class)
#str(y_test)
#length(predictions$class)

#length(y_test)

# summarize results
confusionMatrix(predictions$class, data_test$gender)


####################### NB ROC####################


PredictionNBModel <- NaiveBayes(gender~., data=data_train)
PredictionsWithProbs=predict(PredictionNBModel,data_test, type = 'prob')
#PredictionsWithProbs$posterior
auc=auc(data_test$gender,PredictionsWithProbs$posterior[,2])
NB_ROC=roc(data_test$gender,PredictionsWithProbs$posterior[,2],smooth = TRUE)
plot(NB_ROC,col="blue", lwd=3, main="ROC (Decision Tree) ", xlab="True Positive Rate", ylab="False Positive Rate ")
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
