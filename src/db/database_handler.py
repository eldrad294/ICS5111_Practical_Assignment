import mysql.connector
#
class db():
    #
    """ An example as to how invoke and use this class:
            from src.db.database_handler import db
            #
            db_obj = db('127.0.0.1','yelp_db','root','1234')
            sql = "SELECT * FROM yelp_db.review limit 10;"
            cursor = db_obj.select_query(sql)
            print(cursor)
    """
    def __init__(self, url, db_name, username, password):
        """ DB class constructor """
        self.url = url
        self.username = username
        self.password = password
        self.db_name = db_name
        #
    #
    def connect(self):
        """ DB connect method """
        # Connect with the MySQL Server
        conn = None
        try:
            conn = mysql.connector.connect(user=self.username,
                                           password=self.password,
                                           database=self.db_name,
                                           host=self.url)
            print('Connection established.')
        except Exception as e:
            print(str(e))
        return conn
    #
    def close(self, conn):
        """ Closes DB connection """
        try:
            conn.close()
            print('Connection closed.')
        except Exception as e:
            print(str(e))
    #
    def select_query(self, conn, sql):
        """ Takes an sql query and executes it through the DB. Reserved for select statements """
        try:
            cur = conn.cursor()
            #
            # Executes the sql statement across the database
            cur.execute(sql)
            #
            # Converts retrieved cursor into list of tuples
            cur = cur.fetchall()
            return cur
        except Exception as e:
            print(str(e))
            #
    def execute_query(self, conn, sql):
        """ Takes an sql query and executes it through the DB. Reserved for insert/update/delete statements """
        try:
            #
            cur = conn.cursor()
            #
            # Executes the sql statement across the database
            cur.execute(sql)
            #
            conn.commit()
            print('SQL Executed!')
        except Exception as e:
            print(str(e))
