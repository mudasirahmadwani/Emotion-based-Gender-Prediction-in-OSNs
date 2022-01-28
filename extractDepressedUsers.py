import tweepy
import time
import csv
access_token = "326604560-qmrVWFtRW1qkNZNKJS3ZOhqouYafiql1dkb9dTEe"
access_token_secret = "i86GQbuEnJdlYV0bRUsJHND9D6bMROmRx53FBZ81bBpHe"
consumer_key = "nBxlK3FCdrf14fb8nNMslMUJU"
consumer_secret = "FiAffQVvUI3ZcrDUQ42YdHUmUBxtySERt6e4udeU3uQ4m5WBJC"
print("Data Extraction")
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth,wait_on_rate_limit=True)

#f3 = open("D:\Desktop\Mudasir\Depression\self declared twitter user-old.csv", 'w');
f3 = open("C:/Users/mudasirw/Documents\DATA-mudasir/keyword-based-depressed-users-extracted.csv", 'w');

#f3 = open("C:\Users\mudasirw\Documents\DATA-mudasir\keyword-based-users-extracted", 'w');
# Open/Create a file to append data
#csvFile = open('D:\Desktop\Mudasir\Depression\self declared twitter user.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile,quoting=csv.QUOTE_NONNUMERIC)

#while (1):
for pages in tweepy.Cursor(api.search,q=" (i am) OR (i suffer depress) OR (i taking antidepressant drugs) OR (depression hitting me) OR (i hit depress) OR (i battling depression) OR (i depression attack) OR (depress)", until="2019-02-04",lang="en",tweet_mode='extended').pages():
    #print (tweet.created_at, tweet.text.encode('utf-8'))
   #print tweet.in_reply_to_status_id
    for tweet in pages:
        if((tweet.in_reply_to_status_id is None) or not(tweet.retweeted)):
            print (tweet.created_at)
            print (tweet.user.screen_name)
            print (tweet.full_text)
            print (tweet.retweeted)
            #print"...................."
           # csvWriter.writerow((tweet.user.screen_name, tweet.created_at, tweet.full_text.encode('utf-8')))
            f3.write(str(tweet.user.screen_name)+"\t"+str(tweet.created_at)+"\t"+tweet.full_text.encode('utf-8')+"\n")
    print ("**********************")
    print(tweet.full_text)



    '''
    print tweet.created_at
    print "......................"
    print tweet.full_text
    print "###############"

    print tweet.user.screen_name
    print "......................"
    csvWriter.writerow([(tweet.user.screen_name,tweet.created_at)])
    '''