import tweepy
import time
import configparser
import json
import os
import argparse


def send_dm(api,user_id="1480098116",msg="sample msg"):
    api.send_direct_message(recipient_id=user_id,text=msg)

def get_user_favorites(api,username):
    favs = api.favorites(id=username)
    print(favs[0]._json["user"]["screen_name"])


if __name__ == "__main__":
    FOLLOWERS_JSON="followers.json"

    config = configparser.ConfigParser()
    config.read('config/auth.ini')
    
    consumer_key = config['Authorization']['CONSUMER_KEY']
    consumer_secret = config['Authorization']['CONSUMER_SECRET']
    access_token_key = config['Authorization']['ACCESS_TOKEN_KEY']
    access_token_secret = config['Authorization']['ACCESS_TOKEN_SECRET']
    MSG = config['USER_INFO']['MESSAGE_TO_SEND']
    PRIMARY_USER = config['USER_INFO']['HANDLE']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    # Find all of the primary user's followers
    if not os.path.exists(FOLLOWERS_JSON):
        followers = api.followers_ids(screen_name=PRIMARY_USER)
        with open(FOLLOWERS_JSON, 'w') as outfile:
            json.dump(followers, outfile)
        print("Found every follower.")

    # If file exists, just read through it without making api call
    with open(FOLLOWERS_JSON) as f:
        followers = json.load(f)

    # Send DMs
    for follower in followers:
        send_dm(api,user_id=follower,msg=MSG)
    
    """favorites = {}
    for follower in followers:
        relevant_favs = 0
        for favorite in tweepy.Cursor(api.favorites, id=follower).items(20):
            if favorite._json["user"]["screen_name"] == PRIMARY_USER:
                relevant_favs += 1
        favorites[follower] = relevant_favs
    print(favorites)"""


    # get_user_favorites(api,username="nebbrooks")

    # send_dm(api)