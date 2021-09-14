import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))

api = tweepy.API(auth)
client = tweepy.Client(
    bearer_token=os.getenv("bearer_token"),
    consumer_key=os.getenv("consumer_key"),
    consumer_secret=os.getenv("consumer_secret"),
    access_token=os.getenv("access_token"),
    access_token_secret=os.getenv("access_token_secret"),
    wait_on_rate_limit=True,
)

list_name = "Elon Musk's Feed"
list_description = "A list of everyone Elon Musk follows"

twitter_list = api.create_list(name=list_name, description=list_description)
list_id = twitter_list._json["id"]

twitter_handle = "elonmusk"
user = client.get_user(username=twitter_handle)

followers = client.get_users_following(id=user.data.id, max_results=1000)

for i in range(0, len(followers.data), 100):
    ids = [follower["id"] for follower in followers.data[i : i + 100]]
    api.add_list_members(list_id=list_id, user_id=ids)
