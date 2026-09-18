import os

import tweepy
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("X_API_KEY")
api_key_secret = os.getenv("X_API_KEY_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

print("\n--- NEORUINS LIVE X PUBLISHING TEST ---")
print("WARNING: This utility can create a REAL public Post on X.")
print("It is intended only for testing your own NEORUINS X integration.")

if not all([
    api_key,
    api_key_secret,
    access_token,
    access_token_secret,
]):
    print("\nERROR: One or more X credentials are missing.")
    raise SystemExit

try:
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    account = client.get_me(user_auth=True)

    if not account.data:
        print("\nERROR: Could not verify the X account.")
        raise SystemExit

    username = account.data.username

    test_post = "Testing the NEORUINS bot connection. 🎮"

    print(f"\nConnected account: @{username}")
    print("\nThe following Post will be published if you confirm:")
    print()
    print(test_post)
    print()
    print(f"Destination account: @{username}")
    print()
    print("WARNING: Publishing will create a REAL public Post on X.")
    print("If you only wanted to verify that this script loads, cancel here.")

    confirmation = input(
        '\nType exactly "YES" to publish, or anything else to cancel: '
    ).strip()

    if confirmation != "YES":
        print("\nCANCELLED: Nothing was published.")
        raise SystemExit

    response = client.create_tweet(
        text=test_post,
        user_auth=True,
    )

    if response.data:
        post_id = response.data["id"]

        print("\nSUCCESS: The test Post was published.")
        print(f"Post ID: {post_id}")
        print(f"Account: @{username}")
    else:
        print("\nERROR: X did not return Post information.")

except tweepy.TweepyException as error:
    print("\nERROR: X API request failed.")
    print(error)