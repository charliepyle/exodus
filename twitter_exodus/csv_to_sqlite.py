from db_functions import select_follower_by_id, insert_follower, messaged_follower, delete_follower
from db_init import create_connection, db_init

def main():
    database = r"twitter_exodus.db"
    
    
    

    # create a database connection
    conn = create_connection(database)

    # create tables
    with conn:
        
        # TODO -- integrate with csv    

if __name__ == '__main__':
    main()