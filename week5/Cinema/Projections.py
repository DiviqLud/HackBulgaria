import sqlite3
import ast
#from Movies import show_movies
from datetime import datetime


class Projections():
    def __init__(self, cursor):
        result = cursor.execute('''SELECT id, movie_id, movie_type, date_time
                                       FROM Projections''')
        for row in result:
            self.id = row['id']
            self.movie_id = row['movie_id']
            self.movie_type = row['movie_type']
            self.date_time = row['date_time']
        self.seats = []
        self.spots = 100
        self.all_seats = []

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

    def checking_movie_for_spots(self, cursor, movie_id):
        self.select_title(cursor, movie_id)

        result = cursor.execute(''' SELECT id,
                                           movie_id,
                                           date_time,
                                           movie_type
                                    FROM Projections
                                    WHERE movie_id = ?''', (movie_id, ))
        result = result.fetchall()

        for row in result:
            print(str(row['id']) + ' - ' + row['date_time'] + ' (' + row['movie_type'] + ') ' + str(self.take_spots(cursor, row['id'])) + " available spots")

    def take_spots(self, cursor, projection_id):
        self.spots = 100
        result = cursor.execute("SELECT count(*) FROM Reservations WHERE projection_id = ?", (projection_id, ))
        counter = result.fetchone()
        self.spots -= counter[0]
        return self.spots

    def show_seats_for_projection(self, cursor, projection_id):
        result = cursor.execute("SELECT id from Projections")
        for row in result:
            if row['id'] == int(projection_id):
                self.taken_seats(cursor, projection_id)

    def print_seats(self, cursor):
        self.seats[0][0] = '  '

        for k in range(1, 11):
            self.seats[0][k] = str(k) + " "

        for k in range(1, 11):
            self.seats[k][0] = str(k) + " "
            if k == 10:
                self.seats[k][0] = str(k)

        for i in range(11):
            print("".join(str(x) for x in self.seats[i]))

    def check_seats_for_out_index(self, cursor, string):
        place = ast.literal_eval(string)
        if place[0] > 10 or place[0] < 0 or place[1] > 10 or place[1] < 0:
            print("There is no seat like this one!")
            return False
        else:
            return True

    def taken_seats(self, cursor, projection_id):
        result = cursor.execute("SELECT row, col FROM Reservations WHERE projection_id = ?", (projection_id))
        self.seats = [[". " for x in range(11)] for x in range(11)]
        for row in result:
            self.seats[row['row']][row['col']] = 'x '
            self.spots -= 1
        self.print_seats(cursor)

    def check_seats_if_available(self, cursor, string):
        place = ast.literal_eval(string)
        if self.check_seats_for_out_index(cursor, string) is True:
            if self.seats[place[0]][place[1]] == 'x ':
                print("This seat is taken!")
                return False
            else:
                return True

    def take_seats(self, cursor, string, projection_id):
        place = ast.literal_eval(string)
        if self.seats[place[0]][place[1]] == ". ":
            self.seats[place[0]][place[1]] = "x "
            self.spots -= 1
            self.all_seats.append(place)

    def print_reservation(self, cursor, movie_id, projection_id):
        print("This is your reservation: ")
        result = cursor.execute(''' SELECT name, rating FROM Movies WHERE id = ?''', (movie_id,))
        for row in result:
            print("Movie: " + row['name'] + " (" + str(row['rating']) + ")")
        result = cursor.execute(''' SELECT date_time, movie_type
                                    FROM Projections
                                    WHERE id = ?''', (projection_id,))
        for row in result:
            print("Date and time: " + row['date_time'] + " (" + row['movie_type'] + ")")
        seats = " "
        for seat in self.all_seats:
            seats += str(seat)
        print("Seats: " + seats)

    def commit_taken_seats_in_db(self, cursor, conn, final_command, username, projection_id, seats):
        place = ast.literal_eval(seats)
        if final_command.lower() == "finalize":
            cursor.execute(''' INSERT INTO Reservations(username,
                                                        projection_id,
                                                        row,
                                                        col)
                               VALUES(?, ?, ?, ?)''',
                                (username, projection_id, place[0], place[1]))

            conn.commit()
        self.all_seats = []

    def give_up(self):
            print("You can give up if you want!")
            give_up = input("Enter command for give up> ")
            if give_up == "give up":
                self.menu()


    def menu(self):
        print(''' Welcome to your cinema!
                  Here are the things you can do:
                        1. add_movie
                        2. show_movies
                        3. add_projection
                        4. show_movie_projections <movie_id>
                        5. show_movie_projections_by_date <movie_id> <date_time>
                        6. make_reservation''')
        command = input("Enter your choice: ")
        return command