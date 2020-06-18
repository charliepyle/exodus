from db_functions import select_follower_by_id, insert_follower, messaged_follower, delete_follower
from db_init import create_connection, db_init
import pandas as pd

def main():
    database = r"twitter_exodus.db"
    
    
    

    # create a database connection
    conn = create_connection(database)

    # create tables
    with conn:
        df = pd.read_csv('results/tweets.csv', delimiter=',')
        for _, row in df.iterrows():
            follower_tuple = (row['user_id'], 0, 0, 0)
            insert_follower(conn, follower_tuple)
        
        # TODO -- integrate with csv    

if __name__ == '__main__':
    main()