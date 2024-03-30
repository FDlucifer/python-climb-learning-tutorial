from os import access
from matplotlib import colors
import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

all_keys = open('twitterkeys', 'r').read().splitlines() # put your twitter development keys here...

api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)
crypto_currency = 'Dogecoin' # here you can also change to "Bitcoin"

start = "2021-04-04" # can change start and end time here
end = "2021-04-05"

search = f'#{crypto_currency} -filter:retweets'
tweet_cursor = tweepy.Cursor(api.search, q=search, lang='en', until=end, since=start, tweet_mode='extended').items(500)
tweets = [tweet.full_text for tweet in tweet_cursor]
tweets_df = pd.DataFrame(tweets, columns=['Tweets'])
for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets'])

tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']

plt.bar([0, 1], [positive, negative], label=['Positive', 'Negative'], color=['green', 'red'])
plt.legend()

plt.show()