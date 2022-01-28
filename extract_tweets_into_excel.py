import tweepy
import time
import csv
import codecs
import json
import xlsxwriter
from tweepy import OAuthHandler
access_token = "326604560-qmrVWFtRW1qkNZNKJS3ZOhqouYafiql1dkb9dTEe"
access_token_secret = "i86GQbuEnJdlYV0bRUsJHND9D6bMROmRx53FBZ81bBpHe"
consumer_key = "nBxlK3FCdrf14fb8nNMslMUJU"
consumer_secret = "FiAffQVvUI3ZcrDUQ42YdHUmUBxtySERt6e4udeU3uQ4m5WBJC"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth,wait_on_rate_limit=True)



#f3 = codecs.open("C:/Users/mudasirw/Documents\DATA-mudasir/keyword-based-users-extracted.xlsx", 'w', encoding='utf-8');
for pages in tweepy.Cursor(api.search,q="(*)",lang="ar",tweet_mode='extended').pages():
#for pages in tweepy.Cursor(api.search,q="war",lang="en", tweet_mode='extended').pages():
    #print (tweet.created_at, tweet.text.encode('utf-8'))
   #print tweet.in_reply_to_status_id
    for tweet in pages:
        if((tweet.in_reply_to_status_id is None) and not(tweet.full_text[:2]=="RT")):
            print(tweet.created_at)
            print(tweet.user.screen_name)
            print(tweet.full_text)
            print(tweet.retweeted)
            print("....................")
           # csvWriter.writerow((tweet.user.screen_name, tweet.created_at, tweet.full_text.encode('utf-8')))
          #  File_object.write(str(tweet.user.screen_name)+"\t"+str(tweet.created_at)+"\t"+str(tweet.full_text.encode('utf-8-sig'))+"\n")

       # f3.write(str(tweet.user.screen_name) + "\t" + str(tweet.created_at) + "\t" + str(tweet.full_text.encode('utf-8-sig')) + "\n")
            workbook = xlsxwriter.Workbook('C:/Users/mudasirw/Documents\DATA-mudasir/tweet_new.xlsx')
            worksheet = workbook.add_worksheet()
            row = 0
            col = 0
            worksheet.write(row, col, user)
            worksheet.write(row, col + 1, tweet)
            row += 1

workbook.close()

print("**********************")

'''
print(tweet.created_at)
print("......................")
print(tweet.full_text)
print("###############")
#print tweet.author._json['screen_name']
print tweet.user.screen_name
print "......................"
csvWriter.writerow([(tweet.user.screen_name,tweet.created_at)])
'''