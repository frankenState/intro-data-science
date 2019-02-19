import tweepy
from textblob import TextBlob

consumer_key = 'SoW6ymh73XmtFbYLspzH0AKpT'
consumer_secret = 'Y6jyFdFcblahtYsY1OuUHLHgrpdmBPU3g1H64ApYPmSu0ZScZ5'

access_token = '1097895123524890624-Sq2emXwCXY4HXBjz2C1LrC3H32DJ9B'
access_token_secret = 'mr1eLViDnGvt7ByCaAKUzEMbaQE7JVIh0YiDoAH4pCuBr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)




