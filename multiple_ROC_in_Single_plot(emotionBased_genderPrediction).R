

#--------------ROC RandomForest ############
gc_pROC_rf <- roc(response = data_test$gender, predictor = gc_prob_rf[, "Male"],smooth = TRUE)
plot(gc_pROC_rf,col="brown",, add=TRUE, lwd=1, main=" ", xlab="True Positive Rate", ylab="False Positive Rate ",
     print.auc=FALSE)

gc_pROC_rf$auc

#--------------SVM ROC ############
plot(gc_pROC,col="blue", add=TRUE, lwd=2.5,
     xlab="False Positive Rate", ylab="True Positive Rate ", smooth=TRUE,lty=2,smooth = TRUE)
gc_pROC$auc

#--------------Naive Bayes ROC ############
plot(NB_ROC,col="black", add = TRUE,lwd=2.5,lty=3)
NB_ROC$auc

#--------------ROC Decision Tree ############
 #plot(gc_pROC_dt,col="blue", lwd=2.5,lty=3, main=" ",add = TRUE,
 #    xlab="True Positive Rate", ylab="False Positive Rate ",
 #    auc.polygon=FALSE)


#--------------ROC KNN ############

gc_pROC_knn <- roc(response = testing$gender, predictor = gc_prob[, "Male"],smooth = TRUE)
plot(gc_pROC_knn,col="#02c3c1", lwd=1, main="",
     xlab="True Positive Rate", ylab="False Positive Rate",
     auc.polygon=TRUE)

gc_pROC$auc





legend(0.7,0.3, legend=c("Random Forest", "Support Vector Machine","Naive Bayes","K-Nearest Neighbors" ),
       col=c("brown", "blue","black","#02c3c1"), lty=1:3, cex=0.6)

