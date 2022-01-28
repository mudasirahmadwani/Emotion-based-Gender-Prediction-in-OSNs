from __future__ import division
from nltk.corpus import stopwords
import xlrd
import string
from nltk.tokenize import word_tokenize
import re
from django.utils.encoding import smart_str, smart_unicode


#Loading sample file
file_location="D:/Desktop/Mudasir/Predicting personality/Python Programming Data/mood_book(full).xlsx"
workbook = xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

#Loading emotion dictionary
file_location="D:/Desktop/Mudasir/Predicting personality/Python Programming Data/emolex_appended_dict.xlsx"
workbook = xlrd.open_workbook(file_location)
emo_dictionary = workbook.sheet_by_index(0)

emoList=emo_dictionary.col_slice(0)
fear = ([i for i in emoList if i.value!=""])
#print (fear)
emoList=emo_dictionary.col_slice(1)
angry =([i for i in emoList if i.value!=""])
emoList=emo_dictionary.col_slice(2)
sad = ([i for i in emoList if i.value!=''])
emoList=emo_dictionary.col_slice(3)
joy = ([i for i in emoList if i.value!=''])
emoList=emo_dictionary.col_slice(4)
surprise = ([i for i in emoList if i.value!=''])
emoList=emo_dictionary.col_slice(5)
disgust = ([i for i in emoList if i.value!=''])
emoList=emo_dictionary.col_slice(6)
trust = ([i for i in emoList if i.value!=''])
emoList=emo_dictionary.col_slice(7)
anticipation = ([i for i in emoList if i.value!=''])


def count_emotions(emoList,postToks):
    i = 0;
    for e in emoList:
        #print[s+" Match" for s in postToks if e.value in s]
        for s in postToks:
            if e.value in s:
                i= i+1;
    return i;
def matched_emotions(emolist,postToks):
    #print emolist
    words = set()
    for e in emolist:
        if e.value != "":
           for s in postToks:
             if e.value == s:
                #print e.value+" hhhhhhhhh "+s
                words.add(s)
    return words;

def mood_Statistics(postToks):

    moodStat=[]
    moodStat.append(count_emotions(fear,postToks))
    moodStat.append(count_emotions(angry, postToks))
    moodStat.append(count_emotions(sad, postToks))
    moodStat.append(count_emotions(joy, postToks))
    moodStat.append(count_emotions(surprise, postToks))
    moodStat.append(count_emotions(disgust, postToks))
    moodStat.append(count_emotions(trust, postToks))
    moodStat.append(count_emotions(anticipation, postToks))
    return(moodStat)

def mood_vector2(postToks):
    total_wor = set()
    #print fear
    fear_wor = matched_emotions(fear,postToks)
    #print angry
    angry_wor = matched_emotions(angry, postToks)
    #print sad
    sad_wor = matched_emotions(sad, postToks)
    joy_wor = matched_emotions(joy, postToks)
    surprise_wor = matched_emotions(surprise, postToks)
    disgust_wor = matched_emotions(disgust, postToks)
    trust_wor = matched_emotions(trust, postToks)
    anti_wor = matched_emotions(anticipation, postToks)
    total_wor = fear_wor|angry_wor|sad_wor|joy_wor|surprise_wor|disgust_wor|trust_wor|anti_wor

    f = fear_wor.__len__()
    a = angry_wor.__len__()
    s = sad_wor.__len__()
    j = joy_wor.__len__()
    su = surprise_wor.__len__()
    d = disgust_wor.__len__()
    t = trust_wor.__len__()
    a = anti_wor.__len__()
    #print str(f)+" "+str(a)+" "+str(s)+" "+str(j)+" "+str(su)+" "+str(d)+" "+str(t)+" "+str(a)
    #print str(f)+" "+str(a)
    #print total_wor.__len__()
    total = total_wor.__len__()
    moodVector = [0, 0, 0, 0, 0, 0, 0, 0]

    if total:
        #print "heloo"
        moodVector[0] = f / total
        moodVector[1] = a / total
        moodVector[2] = s / total
        moodVector[3] = j / total
        moodVector[4] = su / total
        moodVector[5] = d / total
        moodVector[6] = t / total
        moodVector[7] = a / total
    return moodVector


def mood_max(postToks):
    moodStat = mood_Statistics(postToks)
    maxMood = max(moodStat)
    max_index = [i + 1 for i, j in enumerate(moodStat) if j == maxMood]
    # max_index = moodStat.index(max(moodStat))
    return (max_index)

def mood_vector(postToks):
    moodStat = mood_Statistics(postToks)
    totalemoWords = sum(moodStat)
    print(totalemoWords)
    moodVector = [0,0,0,0,0,0,0,0]
    if(totalemoWords):
        moodVector = [round(float(i)/totalemoWords,3) for i in moodStat]
    return (moodVector)


##### Normalization############
def norml(str):
    final_word = "";
    str = str.lower();
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(str)
    nor_str = "";
    punctuations = list(string.punctuation);
    for w in words:
        if w not in stop_words and w not in punctuations:
            nor_str = nor_str + " " + w;
    final_word=word_tokenize(nor_str)
    return(final_word);


f = open("D:/Desktop/Mudasir/Predicting personality/Python Programming Data/testing_post_content2.csv", 'w');
#f2 = open("D:/Desktop/Mudasir/Predicting personality/Python Programming Data/mood_plot_data(in).csv", 'w');
f3 = open("D:/Desktop/Mudasir/Predicting personality/Python Programming Data/mood_cluster_data(equal).csv", 'w');
i = 0;userCount = 1;
while i < sheet.nrows:
   content=""
   user_id= sheet.cell_value(i, 0)
   content = sheet.cell_value(i, 4) + " " + sheet.cell_value(i, 5)
   #print("value before", i);
   prev_id=sheet.cell_value(i, 0)
   coverName = sheet.cell_value(i, 1)
   label = sheet.cell_value(i, 2)

   i = i + 1;
   next_id = sheet.cell_value(i, 0)

   while(prev_id==next_id):
       #content = content + sheet.cell_value(i, 4) + " " + sheet.cell_value(i, 5)
       postC = (sheet.cell_value(i, 4))
       postC = repr(postC)
       content = content + postC + " ";
       prev_id=next_id;
       i=i+1;
       next_id=sheet.cell_value(i, 0)

   nor_content=norml(content); #calling norl function
   #print(prev_id);
   #print (content);

   #print("u"+str(userCount)+"\t")
   mood_vector2(nor_content)
   #print(mood_Statistics(content));
   #print(" Fear Match "+ str(count_emotions(fear,content)));

   #f.write("u"+str(userCount)+"\t"+coverName+"\t")
   #moodMaxStat = mood_max(content)
   #moodStatStd = [0,0,0,0,0,0,0,0]
   #for k in range(0,len(moodMaxStat)):
       #moodStatStd[k] = moodMaxStat[k]
   #str2= "\t".join(str(i) for i in moodStatStd)
   #f.write(str2)
   #f.write("\n");
   #allContent = re.sub(r'[^\x00-\x7F]+', '', allContent)
   #f.write(allContent)
   #f.write("\n");
   #moodStat = mood_Statistics(content)
   #str2 = "\t".join(str(i) for i in moodStat)
   #f.write(str2)
   #f.write("\n");

   moodVector = mood_vector2(nor_content)
   moodStr = "\t".join(str(i) for i in moodVector)
   f3.write("u"+str(userCount)+"\t"+moodStr+"\t"+label+"\n")

   #for k in range(0,len(moodMaxStat)):
       #f2.write(str(userCount)+"\t"+str(moodMaxStat[k])+"\t"+label+"\n")


   userCount = userCount + 1;
   #f.write(prev_id);
   #f.write(smart_str(content)+"\n");


f.close()

