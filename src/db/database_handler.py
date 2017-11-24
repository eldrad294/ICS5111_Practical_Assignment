import mysql
class db():
    #
    def __init__(self,url,username,password):
        """ DB class constructor """
        self.url = url
        self.username = username
        self.password = password
    #
    def connect(self):
        """ DB connect method """
