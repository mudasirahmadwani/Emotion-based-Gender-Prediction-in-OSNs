library(ggplot2)
mydata=read.csv(file.choose())

anyNA(mydata)
dim(mydata)
mydata_female=mydata[2:692,]
mydata_male=mydata[693:1563,]
mydata_female=mydata[2:485,]
mydata_male=mydata[486:939,]
dim(mydata_female)
dim(mydata_male)
#mydata[mydata==0]<-0.01
stats(mydata_female)
x=c(1:length(mydata_female$UserId))
mud_data_df1=as.data.frame(cbind(x, mydata))
head(mud_data_df1)

female_data_frm=as.data.frame(cbind(x, mydata_female))

#Negative emotion fraction in Female users/Fake users

sp=ggplot(female_data_frm, aes(x=x, y=female_data_frm$negativeFrac))+geom_point(color="#ec796c")+ylim(0.0, 1.0)+xlab("Fake Users")+ylab("negative_frac")
sp

par(mar=c(7,3,3,1))
boxplot(mydata_female$positive,mydata_male$positive,mydata_female$negative,mydata_male$negative,main="Twitter Positive(A11) and Negative (A12) Emotion fractions",
        ylab="Fraction of posts with emotions",  col=c("#ec796c","#02c3c1","#ec796c","#02c3c1"),
        names = c(expression(paste("Female (A"["11"],")")) ,expression(paste("Male (A"["11"],")")), expression(paste("Female (A"["12"],")")), expression(paste("Male (A"["12"],")"))))

#Emotion Categories 
f=boxplot(mydata_female$X.Emo_Categories,mydata_male$X.Emo_Categories,ylab="No. of emotion categories",
        col=c("#ec796c","#02c3c1"),main="#Emotion Categories Female vs Male on Twitter",
        names = c(expression(paste("Female (f"["11"],")")) ,expression(paste("Male (f"["11"],")"))))

boxplot(mydata_female$EmoVariance,mydata_male$EmoVariance,ylab="Emotion Varaince",
        col=c("#ec796c","#02c3c1"),main="Emotion Variance Female vs Male on Twitter",
        names = c(expression(paste("Female (f"["12"],")")) ,expression(paste("Male (f"["12"],")")))
        )


#Real users

real_data_frm=as.data.frame(cbind(x, mydata_male))
sp=ggplot(real_data_frm, aes(x=x, y=mydata_male$negativeFrac))+geom_point(color="#02c3c1")+ylim(0.0, 1.0)+xlab("Real Users")+ylab("negative_frac")
sp




#BOX PLOTS FOR EMOTION FEATURES
par(mar=c(7,5,1,1))
#fake users
#boxplot(mydata_female$fear,mydata_female$anger,mydata_female$sad,mydata_female$joy, mydata_female$surprise, mydata_female$disgust,mydata_female$trust,mydata_female$anticipation)

x=boxplot(mydata_female$fear,mydata_female$anger,mydata_female$sad,mydata_female$joy, mydata_female$surprise, mydata_female$disgust,mydata_female$trust,mydata_female$anticipation,
        data=mydata_female,ylab="Female Users",width=NULL,
        col="#ec796c", las=2, names=c("Fear","Anger","Sad","Joy","Surprise","Disgust","Trust","Anticipation"))

x

#real users
y=boxplot(mydata_male$fear,mydata_male$anger,mydata_male$sad,mydata_male$joy,mydata_male$surprise, mydata_male$disgust,mydata_male$trust,mydata_male$anticipation)
boxplot(mydata_male$fear,mydata_male$anger,mydata_male$sad,mydata_male$joy,mydata_male$surprise, mydata_male$disgust,mydata_male$trust,mydata_male$anticipation,
        data=mydata_male,ylab="Male Users",col="#02c3c1", las=2, names=c("Fear","Anger","Sad","Joy","Surprise","Disgust",
                                                     "Trust","Anticipation"))




