import sqlite3
import Movies
import Projections
import Reservations


conn = sqlite3.connect("cinema.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

proj = Projections.Projections(cursor)
movie = Movies.Movies(cursor)
reservation = Reservations.Reservations(cursor)
print(''' Welcome to your cinema!
          Here are the things you can do:
                1. add_movie
                2. show_movies
                3. add_projection
                4. show_movie_projections <movie_id>
                5. show_movie_projections_by_date <movie_id> <date_time>
                6. make_reservation''')
command = input("Enter your choice: ")
put = command.split(" ")

while put[0] != "end":
    if put[0] == "add_movie" or put[0] == '1':
        movie.add_movie(cursor, conn)
    if put[0] == "show_movies" or put[0] == '2':
        movie.show_movies(cursor)
    if put[0] == "add_projection" or put[0] == '3':
        proj.add_projections(cursor, conn)
    if put[0] == "show_movie_projections":
        proj.show_movie_projections_by_id(cursor, put[1])
    if put[0] == "show_movie_projections_by_date":
        proj.show_movie_projections_by_date(cursor, put[1], put[2])
    if put[0] == "make_reservation" or put[0] == '6':
        username_command = input("Step 1 (USER): Choose name> ")
        number_of_tickets = input("Step 1 (USER): Choose number of tickets> ")
        movie.show_movies(cursor)
        choice_for_movie = input("Step 2 (Movie): Choose a movie> ")
        reservation.helping_func(cursor, choice_for_movie)
    command = input("Enter your choice: ")
    put = command.split(" ")
