import tweepy

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

# Get all the people the user follows
friends = api.friends_ids()

# Print out each one
for id in friends:
    print(id)
