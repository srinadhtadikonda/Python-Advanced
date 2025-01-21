import tweepy

# Your API keys and access tokens
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAADOAyQEAAAAAzSPuwD1cefrMQM97xViycYoD4tA%3DSmjkZNH8vA1oLoZZBgEYKNAl1uJQ34MviDJsRo9SRET5dtdkcV'  # Replace with your actual Bearer Token
API_KEY = 'vmItk283AdAVSZuUtG4dRubpJ'
API_SECRET_KEY = 'UwjByc71l4mrjezmEu7g9z4VglA9ENfr4e5TsIPFxcUlDHgTpZ'
ACCESS_TOKEN = '1103286637222457345-mRyKptzN3Y37X1rT6Yk5nQw7gxwlGM'
ACCESS_TOKEN_SECRET = 'K5wRcFHtNYBfAIVJjWgsHispoEayXTeOTuiHmEU4HrInY'

# Create a Tweepy client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Post a tweet
response = client.create_tweet(text="Hello, world! This is Sourav")

# Print the tweet ID and display the tweet
tweet_id = response.data['id']
print(f"Tweet posted successfully with ID: {tweet_id}")

# Fetch the tweet to display it on the wall
tweet = client.get_tweet(tweet_id)
print(f"Posted Tweet: {tweet.data['text']}")
