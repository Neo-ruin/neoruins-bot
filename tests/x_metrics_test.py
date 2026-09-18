import os

import tweepy
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("X_API_KEY")
api_key_secret = os.getenv("X_API_KEY_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

if not all([
    api_key,
    api_key_secret,
    access_token,
    access_token_secret,
]):
    print("ERROR: One or more X credentials are missing.")
    raise SystemExit


client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


print("\n--- NEORUINS X METRICS TEST ---")
print("This test retrieves metrics for an existing X Post.")
print("No post will be published or changed.")

post_id = input("\nEnter an X Post ID, or press Enter to cancel: ").strip()

if not post_id:
    print("\nMetrics test cancelled.")
    raise SystemExit

if not post_id.isdigit():
    print("\nERROR: X Post ID must contain numbers only.")
    raise SystemExit

print(f"\nTesting X Post ID: {post_id}")
print("Retrieving metrics from X...\n")

try:
    response = client.get_tweet(
        post_id,
        tweet_fields=[
            "created_at",
            "public_metrics",
            "non_public_metrics",
            "organic_metrics",
        ],
        user_auth=True,
    )

    if response.data is None:
        print("ERROR: X did not return post data.")
        raise SystemExit

    print("SUCCESS: X returned the post.")
    print(f"Post ID: {response.data.id}")
    print(f"Created At: {response.data.created_at}")
    print(f"Public Metrics: {response.data.public_metrics}")
    print(f"Non-Public Metrics: {response.data.non_public_metrics}")
    print(f"Organic Metrics: {response.data.organic_metrics}")

except tweepy.TweepyException as error:
    print("X API ERROR:")
    print(error)