from connection3 import MySql

class Actor:

    def getAllActors(self):

        a = MySql() 
        a.execute(sql="SELECT * FROM Actor ORDER BY last_name")

        data = a.fetchall()
        a.closeConnection()

        return data  


    

final = Actor()
print(final.getAllActors())






    


