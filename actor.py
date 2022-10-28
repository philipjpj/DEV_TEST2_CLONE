from connection3 import MySql

class Actor:

    def getAllActors(self):

        a = MySql() 
        a.execute(sql="SELECT * FROM Actor")

        data = a.fetchall()
        a.closeConnection()

        return data  


    def getAllActorsById(self, actorId):

        a = MySql() 
        a.execute(sql=f"SELECT first_name, last_name \
                        FROM actor a \
                        WHERE a.actor_id = '{actorId}'")

        data = a.fetchall()
        a.closeConnection()

        return data  


    # def getAllActorsByFilm(self, filmTitle):

    #     b = MySql()   ##ho l'istanza della classe MySql in a
    #     b.execute(sql=f"SELECT first_name, last_name \
    #                    FROM film f, film_actor fa, actor a \
    #                    WHERE f.film_id = fa.film_id AND a.actor_id = fa.actor_id \
    #                    AND f.title='{filmTitle}'")

    #     data = b.fetchall()
    #     b.closeConnection() ## per chiudere la connessione

final = Actor()
print("Inserisci l'Id dell'attore")
actorId = int(input())
print(final.getAllActorsById(actorId))






    


