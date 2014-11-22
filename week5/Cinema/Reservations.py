import sqlite3
import ast
import Projections


class Reservations():
    def __init__(self, cursor):
        result = cursor.execute('''SELECT id, username, projection_id, row, col
                                       FROM Reservations''')
        for row in result:
            self.id = row['id']
            self.username = row['username']
            self.projection_id = row['projection_id']
            self.row = row['row']
            self.col = row['col']


    def checking_movie_for_spots(self, cursor, string):
        proj = Projections.Projections(cursor)
        proj.select_title(cursor, string)

        result = cursor.execute(''' SELECT id,
                                           movie_id,
                                           date_time,
                                           movie_type
                                    FROM Projections''')
        for row in result:
            if row['movie_id'] == int(string):
                print(str(row['id']) +  ' - ' + row['date_time'] + ' (' + row['movie_type'] + ') ' + str(proj.spots) + " available spots")

    def show_seats_for_projection(self, cursor, string):
        result = cursor.execute("SELECT id from Projections")
        for row in result:
            if row['id'] == int(string):
                self.print_seats(cursor, string)

    def print_seats(self, cursor, string):
        proj.seats[0][0] = '  '

        for k in range(1, 11):
            proj.seats[0][k] = str(k) + " "

        for k in range(1, 11):
            proj.seats[k][0] = str(k) + " "
            if k == 10:
                proj.seats[k][0] = str(k)

        for i in range(11):
            print("".join(str(x) for x in proj.seats[i]))

    def check_seats_for_out_index(self, cursor, string):
        place = ast.literal_eval(string)
        if place[0] > 10 or place[0] < 0 or place[1] > 10 or place[1] < 0:
            return False
        else:
            return True

    def check_seats_if_available(self, cursor, string):
        place = ast.literal_eval(string)
        proj = Projections.Projections(cursor)
        if self.check_seats_for_out_index(cursor, string) is True:
            if proj.seats[place[0]][place[1]] == 'x ':
                print("This seat is taken!")
                return False
            else:
                return True

    def take_seats(self, cursor, string, projection_id):
        place = ast.literal_eval(string)
        if self.seats[place[0]][place[1]] == ". ":
            print("BLaBLa")
            self.seats[place[0]][place[1]] == "x "
            self.spots -= 1
        self.
