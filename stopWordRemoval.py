import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pprint

posts = open("C:/Users/mudasirw/Desktop/RESEARCH @N T N U -JULY 2019/GENDER PREDICTION/python scripts/textAnalysis/female_post_content.txt", 'r')
txt1=posts.read()


# Stop word Removal
stop_words=set(stopwords.words("english"))


print("Stop words blow")
print(stop_words)

words=word_tokenize(txt1)

sent=sent_tokenize(txt1)

print("sentences")
pprint.pprint(sent)

filtered_sent=[]
'''
for w in words:
    if w not in stop_words:
        filtered_sent.append(w)
    print("-------------------------------------------------------------------------")
print("Filterred words")
print(filtered_sent)
print("stemming")
# Stemming

ps=PorterStemmer()
for w in filtered_sent:
  print(ps.stem(w))
stem_sent =(ps.stem(w))
#print (stem_sent.upper())


'''