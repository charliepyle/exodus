from db_functions import select_follower_by_id, insert_follower, messaged_follower, delete_follower
from db_init import create_connection, db_init

def insert_dummy_data(conn, follower):
    insert_follower(conn, follower)

def main():
    database = r"twitter_exodus.db"
    
    
    

    # create a database connection
    conn = create_connection(database)

    # create tables
    with conn:
        
        db_init(conn)
        dummy_follower_id = 'Charlie_Pyle' 

        dummy_follower = (dummy_follower_id, '0', '0', '0') # tests insert works
        insert_dummy_data(conn, dummy_follower)

        select_follower_by_id(conn, dummy_follower_id) # tests update + query works
        messaged_follower(conn, ('1', 'Charlie_Pyle'))
        select_follower_by_id(conn, dummy_follower_id)

        delete_follower(conn, (dummy_follower_id)) # tests delete works
        


if __name__ == '__main__':
    main()



