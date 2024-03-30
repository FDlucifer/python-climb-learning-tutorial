from os import access
from textblob import TextBlob
from textblob.en import positive
import tweepy
import sys

mykeys = open('twitterkeys.txt', 'r').read().splitlines() # you can use your own twitter development api key...

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'death'
tweet_amount = 200

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0
neutral = 0
negative = 0


for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswitch(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswitch('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += tweet_polarity
    print(final_text)

print(polarity)

print(f"Amount of positive tweets: {positive}")
print(f"Amount of negative tweets: {negative}")
print(f"Amount of neutral tweets: {neutral}")