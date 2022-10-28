import mysql.connector as mysql
from mysql.connector import Error

class MySql:
    def __init__(self):

        try:
            self.conn = mysql.connect(host= 'localhost', database = 'sakila', user = 'root', password = 'Andreas945!')
            self.cursor = self.conn.cursor()

        except Error as e:    #parametro errore
            self.conn = "none"
            print("Error while connecting to MySQL", e)

    def closeConnection(self):   ##chiuso cursore e conn
        if (self.conn is not None):
                self.cursor.close()
                self.conn.close()

    def execute(self, sql):

        self.cursor.execute(sql)  ##sql stringa della query da effetuare

    def fetchall(self):
        return self.cursor.fetchall()


        




