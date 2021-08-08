# pip install tweepy

import tweepy

access_token = ""
access_token_secret = ""

api_key = ""
api_key_secret = ""


auth = tweepy.QAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

choice = input("enter the hashtag: ")

tweets = tweepy.Cursor(api.search, q=choice).items(100)

for tweet in tweets:
    print(tweet.text)
    print('\n')