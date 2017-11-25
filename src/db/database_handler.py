import mysql.connector
#
class db():
    #
    """ An example as to how invoke and use this class:
            from src.db.database_handler import db
            #
            db_obj = db('127.0.0.1','yelp_db','root','1234')
            sql = "SELECT * FROM yelp_db.review limit 10;"
            cursor = db_obj.execute_query(sql)
            print(cursor)
    """
    def __init__(self, url, db_name, username, password):
        """ DB class constructor """
        self.url = url
        self.username = username
        self.password = password
        self.db_name = db_name
    #
    def __connect(self):
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
    def __close(self, conn):
        """ Closes DB connection """
        try:
            conn.close()
            print('Connection closed.')
        except Exception as e:
            print(str(e))
    #
    def execute_query(self, sql):
        """ Takes an sql query and executes it through the DB """
        conn = None
        try:
            conn = self.__connect()
            #
            cur = conn.cursor(buffered=True)
            cur.execute(sql)
            #
            self.__close(conn)
            return cur
        except Exception as e:
            if conn is not None:
                self.__close(conn)
            print(str(e))
