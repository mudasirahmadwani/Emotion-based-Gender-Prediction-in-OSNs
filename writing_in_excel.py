import json
import csv
import xlsxwriter
import tweepy
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

def tweet_to_xlsx(tweet):
    tweet_list = []
    tweet_list.append([tweet.user.screen_name, tweet.full_text])
    print("TWEET_ LIST")
    print(tweet_list)

    workbook = xlsxwriter.Workbook('C:/Users/mudasirw/Documents\DATA-mudasir/tweet.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for user, tweet in tweet_list:
        worksheet.write(row, col, user)
        worksheet.write(row, col + 1, tweet)
        row += 1

    workbook.close()

results = api.search(q="(*)", lang="ar",tweet_mode='extended' )
for tweet in results:
    print(tweet.user.screen_name, "Tweet:", tweet.full_text)
    tweet_to_xlsx(tweet)