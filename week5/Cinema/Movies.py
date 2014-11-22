import sqlite3


class Movies():
    def __init__(self, cursor):
        result = cursor.execute('''SELECT id, name, rating
                                       FROM Movies''')
        for row in result:
            self.id = row['id']
            self.name = row['name']
            self.rating = row['rating']

    def add_movie(self, cursor, conn):
        name = input("Name of movie: ")
        rating = input("Rating of the movie: ")
        cursor.execute(''' INSERT INTO Movies(name, rating)
                           VALUES (?, ?)''', (name, rating))
        conn.commit()

    def show_movies(self, cursor):
        result = cursor.execute("SELECT id, name, rating FROM Movies")
        for row in result:
            print(str(row['id']) + " - " + row['name'] + ' (' + str(row['rating']) + ')')