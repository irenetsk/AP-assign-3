import tweepy
import argparse

consumer_key = '59j7xN1pSsbhs3uc2jTwt8v2H'
consumer_secret = 'F1XqnSCbt4lBjpLuIoYnGmLfMBFoUVxkUml7CMbTerA3Tk6pEw'
access_key= '35521051-KkPDOLEbZ124WH7qUkDroZA2pQGVUwKsv7zW1xRdl'
access_secret = 'qRyp1x5m9eM4egAI8SUpZzzfm1YBMVKt4ZaG6Ah6E8Bi6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("--number", type = int, default = 1)
args = parser.parse_args()

def get_tweet(): 
    api = tweepy.API(auth) 
    try:
        tweets = api.user_timeline(screen_name=args.username,count=args.number) 
    except tweepy.TweepError:
        print("Something went wrong :(")
    else:
        for tweet in tweets:
            print(tweet.created_at, tweet.text)

get_tweet()