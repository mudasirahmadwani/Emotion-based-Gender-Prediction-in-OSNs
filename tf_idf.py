import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math
import sys
import pprint


posts = open("C:/Users/mudasirw/Desktop/RESEARCH @N T N U -JULY 2019/GENDER PREDICTION/python scripts/textAnalysis/female_post_content.txt", 'r')
text1=posts.read()


def remove_string_special_characters(s):
    #replace special charater
    stripped=re.sub('[^\w\s]', '',s)
    stripped=re.sub('_', '',stripped)

    # Change any whitespace to one space
    stripped=re.sub('\s+',' ', stripped)

    #remove start and end white space
    stripped = stripped.strip()
    return stripped

def get_doc(sent):
    doc_info =[]
    i=0
    for sent in text_sents_clean:
        i+= 1
        count = count_words(sent)
        temp={'doc_id': i, 'doc_length':count}
        doc_info.append(temp)
    return doc_info

def count_words(sent):
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count += 1
    return count

def create_freq_dict(sents):
    i=0
    freqDict_list = []
    for sent in sents:
        i+= 1
        freq_dict={}
        words=word_tokenize(sent)
        for word in words:
            word=word.lower()
            if word in freq_dict:
                freq_dict[word]+=1
            else:
                freq_dict[word]=1
            temp ={'doc_id':i, 'freq_dict': freq_dict}
        freqDict_list.append(temp)
    return freqDict_list


#function to get TF score
def computeTF(doc_info, freqDict_list):
    TF_scores=[]
    for tempDict in freqDict_list:
        id = tempDict['doc_id']
        for k in tempDict['freq_dict']:
            temp= {'doc_id' : id,
                   'TF_score' : tempDict['freq_dict'][k]/doc_info[id-1]['doc_length'],
                   'key' :k}
            TF_scores.append(temp)
    return TF_scores

#compute IDF
def computeIDF(doc_info, freqDict_list):
    IDF_scores=[]
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count= sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp ={'doct_id': counter, 'IDF_score' : math.log(len(doc_info)/count), 'key': k}

            IDF_scores.append(temp)
    return IDF_scores

#compute TFIDF
def computeTFIDF (TF_scores, IDF_scores):
    TFIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['key']==i['key'] and j['doc_id']==i['doc_id']:
                temp ={'doc_id' : j['doc_id'],
                       'TFIDF_scores' : j['IDF_scores']*['TF_scores'],
                       'key' : i['key']}
        TFIDF_scores.append(temp)
    return TFIDF_scores


#cleaning the punctuation and special characters
text_sents= sent_tokenize(text1)
text_sents_clean = [remove_string_special_characters(s) for s in text_sents]
doc_info = get_doc(text_sents_clean)

freqDict_list = create_freq_dict(text_sents_clean)
TF_scores = computeTF(doc_info, freqDict_list)
IDF_scores = computeIDF(doc_info, freqDict_list)

'''
print("doc_info")
print(doc_info)


print("TF scores")
print (TF_scores)

print("TFIDF scores")
print (IDF_scores)

print("Dictionary")
print (freqDict_list)
'''
print("Dictionary")
pprint.pprint(freqDict_list)

print("TF scores")
pprint.pprint(TF_scores)
print("TFIDF scores")
pprint.pprint(IDF_scores)