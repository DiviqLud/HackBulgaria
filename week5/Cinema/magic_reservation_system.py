import sqlite3
import Movies
import Projections
#import Reservations


conn = sqlite3.connect("cinema.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

proj = Projections.Projections(cursor)
movie = Movies.Movies(cursor)


#def give_up():
#        print("You can give up if you want!")
#        give_up = input("Enter command for give up> ")
#        if give_up == "give up":
#            menu()


#def menu():
#    print(''' Welcome to your cinema!
#              Here are the things you can do:
#                   1. add_movie
#                    2. show_movies
#                    3. add_projection
 #                   4. show_movie_projections <movie_id>
  #                  5. show_movie_projections_by_date <movie_id> <date_time>
   #                 6. make_reservation''')
   # command = input("Enter your choice: ")
   # return command

#if __name__ == '__main__':

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
        proj.give_up()
        choice_for_movie = input("Step 2 (Movie): Choose a movie> ")
        proj.checking_movie_for_spots(cursor, choice_for_movie)
        # CHOOSING PROJECTION
        choice_for_projection = input(
            "Step 3 (Projection): Choose a projection> ")
        proj.show_seats_for_projection(cursor, choice_for_projection)
        # CHOOSING SEATS
        for ticket in range(1, int(number_of_tickets) + 1):
            choice_for_seats = input(
                "Step 4 (Seats): Choose seat " + str(ticket) + "> ")
            while proj.check_seats_for_out_index(
                    cursor, choice_for_seats) is False or proj.check_seats_if_available(
                    cursor, choice_for_seats) is False:
                choice_for_seats = input(
                    "Step 4 (Seats): Choose seat " + str(ticket) + "> ")
            proj.take_seats(cursor, choice_for_seats, choice_for_projection)
        proj.print_reservation(cursor, choice_for_movie, choice_for_projection)
        final_command = input("Step 5 (Confirm - type 'finalize') >")
        for seat in proj.all_seats:
            proj.commit_taken_seats_in_db(cursor,
                                      conn,
                                      final_command,
                                      username_command,
                                      choice_for_projection,
                                      str(seat))

    command = input("Enter your choice: ")
    put = command.split(" ")
