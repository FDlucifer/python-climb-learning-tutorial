# pip install tweepy

import tweepy

access_token = ""
access_token_secret = ""

api_key = ""
api_key_secret = ""


auth = tweepy.QAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print(api)

india_woeid = 23424848

trend_result = api.trends_place(india_woeid)

try:
    for trend in trend_result[0]["trends"][:10]:
        print(trend["name"])
        print(trend["tweet_volume"])

except:
    print("something went wrong...")