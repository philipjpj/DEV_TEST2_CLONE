from connection3 import MySql

class Film:

    def getAllFilm(self):

        a = MySql() 
        a.execute(sql="SELECT title FROM Film")

        data = a.fetchall()
        a.closeConnection()

        return data  




final = Film()
print(final.getAllFilm())






    


