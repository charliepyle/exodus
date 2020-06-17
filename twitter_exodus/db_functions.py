from sqlite3 import Error

# SELECT logic below

def select_follower_by_id(conn, follower_id):
    """
    Query follower by ID
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM followers WHERE follower_id=?", (follower_id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_followers(conn):
    """
    Query all rows in the followers table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM followers")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# INSERT logic below

def insert_follower(conn, follower):
    """
    Insert a follower into the followers table
    :param conn:
    :param follower:
    :return: follower id
    """
    sql = ''' INSERT INTO followers(follower_id,messaged,shared_likes,shared_retweets)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, follower)
    except Error as e:
        print(e)
    
    #return cur.lastrowid unsure if we need to return this value, don't think so

# UPDATE logic below

def messaged_follower(conn, follower):
    """
    update follower so that it's been messaged
    :param conn:
    :param follower:
    :return: follower id
    """
    sql = ''' UPDATE followers
              SET messaged = ?
              WHERE follower_id = ?'''
    cur = conn.cursor()
    try:
        cur.execute(sql, follower)
        conn.commit()
    except Error as e:
        print(e)

# DELETE logic below

def delete_follower(conn, follower_id):
    """
    Delete a follower by task id
    :param conn:  Connection to the SQLite database
    :param follower_id: follower_id of the task
    :return:
    """
    sql = 'DELETE FROM followers WHERE follower_id=?'
    cur = conn.cursor()
    cur.execute(sql, (follower_id,))
    conn.commit()
    
def delete_all_followers(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM followers'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
