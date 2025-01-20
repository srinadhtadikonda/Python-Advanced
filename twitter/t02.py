import tweepy

# Your credentials
API_KEY = 'BJRKEG153RW0WUAx6Uraz70jc'
API_KEY_SECRET = 'MUyXfWHkLfBjiS0EnHu2zKu3DeO5MwlsWrLYzv7ZyTTHTN4yDo'
ACCESS_TOKEN = '1103286637222457345-WWIbDbEypmolaxNXSholGyFRev1but'
ACCESS_TOKEN_SECRET = '8FerfAcFzu3DtfN4tUxDBBSPsiffnEfzTxRkikiHiKG3r'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAInetwEAAAAAWakJaHLtVHylfAVQJV4cIIrbQ1Y%3DA4XAtZeXtqpJLzGBwXCuRnuyct4lVg9IyXSxXp0zllifugfkSV'

# Authenticate to Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Post a tweet
response = client.create_tweet(text="hai how are you today.")
print(f"Tweet posted with ID: {response.data['id']}")
