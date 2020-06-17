import tweepy
import time
import configparser


def send_dm(api,user_id="1480098116",msg="sample msg"):
    api.send_direct_message(recipient_id=user_id,text=msg)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config/auth.ini')
    
    consumer_key = config['Authorization']['CONSUMER_KEY']
    consumer_secret = config['Authorization']['CONSUMER_SECRET']
    access_token_key = config['Authorization']['ACCESS_TOKEN_KEY']
    access_token_secret = config['Authorization']['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    send_dm(api)