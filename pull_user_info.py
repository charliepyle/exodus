import os
import sys

if __name__ == "__main__":
    FOLLOWERS = "results/followers.csv"
    TWEETS = "results/tweets.csv"
    LIKES = "results/likes.csv"

    # Creating results file if it isn't there
    if not os.path.exists("results"):
        os.mkdir("results")


    # Pulling userinformation from CL input
    try:
        username = sys.argv[1]
        print("Username:", username)
        c1 = "twint -u {} -o {} --csv".format(username,TWEETS)
        c2 = "twint -u {} --favorites -o {} --csv".format(username,LIKES)
        c3 = "twint -u {} --followers -o {} --csv".format(username,LIKES)
        os.system(c1)
        os.system(c2)
        os.system(c3)
    except:
        print("Not so valid username.")



    

