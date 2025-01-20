import schedule
import time

def post_tweet():
    api.update_status("This is a scheduled tweet from my bot!")

# Schedule the tweet every 1 hour
schedule.every(1).hours.do(post_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
