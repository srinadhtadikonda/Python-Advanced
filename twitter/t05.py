import tweepy
import os

# Consumer keys and access tokens, used for OAuth
consumer_key	= 'YOUR CONSUMER KEY HERE'
consumer_secret     = 'YOUR CONSUMER SECRET HERE'
access_token	= 'YOUR ACCESS TOKEN HERE'
access_token_secret = 'YOUR ACCESS TOKEN SECRET HERE'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
friends = sorted(api.friends_ids())

friendsFile = open("friends.txt","w")

for id in friends:
    friendsFile.write(str(id) + "\n")

friendsFile.close()
