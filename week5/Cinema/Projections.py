import sqlite3
from datetime import datetime


class Projections():
    def __init__(self, cursor):
        result = cursor.execute(''' SELECT id, movie_id, movie_type, date_time
                                    FROM Projections''')
        for row in result:
            self.id = row['id']
            self.movie_id = row['movie_id']
            self.movie_type = row['movie_type']
            self.date_time = row['date_time']
        self.seats = [[". " for x in range(10)] for x in range(10)]

    def add_projections(self, cursor, conn):
        movie_id = input("Movie id: ")
        movie_type = input("Type of movie: ")
        date_time = input("Time of the projection: ")
        cursor.execute(''' INSERT INTO Projections(movie_id,
                                                   movie_type,
                                                   date_time)
                           VALUES (?, ?, ?)''', (movie_id,
                                                 movie_type,
                                                 date_time))
        conn.commit()

    def show_movie_projections_by_id(self, cursor, string):
        self.select_title(cursor, string)
        self.select_projections(cursor, string)

    def select_title(self, cursor, string):
        name_of_movie = cursor.execute(''' SELECT id, name FROM Movies ''')
        for row in name_of_movie:
            if row['id'] == int(string):
                print("Projections for " + row['name'])

    def select_projections(self, cursor, string):
        result = cursor.execute('''SELECT  id, movie_id, date_time, movie_type
                                   FROM Projections
                                   ORDER BY date_time''')
        for row in result:
            if row['movie_id'] == int(string):
                print(str(row['id']) + " - " + row['date_time'] + ' (' + str(row['movie_type']) + ')')


    def show_movie_projections_by_date(self, cursor, string, time):
        self.select_title_and_date(cursor, string, time)
        self.select_available_times_for_current_date(cursor, string, time)

    def select_title_and_date(self, cursor, string, time):
        movie_name_and_date = cursor.execute(''' SELECT Movies.id,
                                                        Movies.name,
                                                        Projections.date_time
                                                 FROM Movies
                                                 INNER JOIN Projections
                                                 ON Movies.id = Projections.movie_id''')
        for row in movie_name_and_date:
            if row['id'] == int(string):
                time1 = row['date_time'].split(" ")
                if time1[1] == time:
                    print("Projections for " + row['name'] + " on a date " + time1[1])
            break

    def select_available_times_for_current_date(self, cursor, string, time):
        result = cursor.execute(''' SELECT id,
                                           date_time,
                                           movie_type,
                                           movie_id 
                                    FROM Projections
                                    ORDER BY date_time''')
        for row in result:
            if row['movie_id'] == int(string):
                time1 = row['date_time'].split(" ")
                if time1[1] == time:
                    print(str(row['id']) + " - " + time1[0] + ' (' + str(row['movie_type']) + ')')

