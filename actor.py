from connection3 import MySql

class Actor:

    # def getAllActors(self):

    #     a = MySql() 
    #     a.execute(sql="SELECT * FROM Actor")

    #     data = a.fetchall()
    #     a.closeConnection()

    #     return data  


    def getAllActorsByFilm(self, filmTitle):

        b = MySql()   ##ho l'istanza della classe MySql in a
        b.execute(sql=f"SELECT first_name, last_name \
                       FROM film f, film_actor fa, actor a \
                       WHERE f.film_id = fa.film_id AND a.actor_id = fa.actor_id \
                       AND f.title='{filmTitle}'")

        data = b.fetchall()
        b.closeConnection() ## per chiudere la connessione

        return data  #utile quando voglio andare a prendere i valori e richiamarli da un'altra parte come in questo caso (VEDI RIGA 30)

final = Actor()
print(final.getAllActorsByFilm("AFRICAN EGG"))






    


