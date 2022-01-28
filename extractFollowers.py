import tweepy
import time

access_token = "326604560-qmrVWFtRW1qkNZNKJS3ZOhqouYafiql1dkb9dTEe"
access_token_secret = "i86GQbuEnJdlYV0bRUsJHND9D6bMROmRx53FBZ81bBpHe"
consumer_key = "nBxlK3FCdrf14fb8nNMslMUJU"
consumer_secret = "FiAffQVvUI3ZcrDUQ42YdHUmUBxtySERt6e4udeU3uQ4m5WBJC"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
'''
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="McDonalds").pages():
    ids.extend(page)
    print ids
    time.sleep(10)

print len(ids)

#public_tweets = api.home_timeline()
public_tweets = api.user_timeline("iamsrk")
for tweet in public_tweets:
    print(tweet.text)
'''
for tweet in tweepy.Cursor(api.search,q="happy ",count=100, lang="en",since="2017-04-03",tweet_mode='extended').items(10000):


    #print (tweet.created_at, tweet.text.encode('utf-8'))
    print ("......................"),
    print (tweet.full_text)
    print ("###############")
    #print tweet.author._json['screen_name']
    print (tweet.user.screen_name)
    print ("......................"),

    '''
    sname = tweet.author._json['screen_name']
    user_tweets = api.user_timeline(screen_name=sname, count=5,tweet_mode='extended')
    for t in user_tweets:
        print t.full_text
        print "......................"
    '''

user = api.get_user('vkylatherese')
print (user)
