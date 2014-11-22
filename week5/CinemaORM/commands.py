from sqlalchemy import create_engine
from cinema import Cinema
from sqlalchemy.orm import Session
import base


def main():
    engine = create_engine("sqlite:///cinema.db")
    base.Base.metadata.create_all(engine)

    session = Session(bind=engine)

    print(''' Welcome to your cinema!
                  Here are the things you can do:
                        1. add_movie
                        2. show_movies
                        3. add_projection
                        4. show_movie_projections <movie_id>
                        5. make_reservation''')
    command = input("Enter your choice: ")
    put = command.split(" ")

    cinema = Cinema(session)

    while put[0] != "end":
        if put[0] == "add_movie" or put[0] == '1':
            cinema.add_movie()
        if put[0] == "show_movies" or put[0] == '2':
            cinema.show_movies()
        if put[0] == "add_projection" or put[0] == '3':
            cinema.add_projections()
        if put[0] == "show_movie_projections":
            cinema.show_movie_projections_by_id(put[1])
        if put[0] == "make_reservation" or put[0] == '5':

            #ENTER INFORMATION FOR USER

            username_command = input("Step 1 (USER): Choose name> ")
            number_of_tickets = input("Step 1 (USER): Choose number of tickets> ")
            cinema.show_movies()
            #cinema.give_up()

            #CHOOSING MOVIE

            choice_for_movie = input("Step 2 (Movie): Choose a movie> ")
            cinema.checking_movie_for_spots(choice_for_movie)

            # CHOOSING PROJECTION

            choice_for_projection = input(
                "Step 3 (Projection): Choose a projection> ")
            cinema.show_seats(choice_for_projection)

            # CHOOSING SEATS

            for ticket in range(1, int(number_of_tickets) + 1):
                choice_for_seats = input(
                    "Step 4 (Seats): Choose seat " + str(ticket) + "> ")
                while cinema.check_seats_for_out_index(
                        choice_for_seats) is False or cinema.check_seats_if_available(
                        choice_for_seats) is False:
                    choice_for_seats = input(
                        "Step 4 (Seats): Choose seat " + str(ticket) + "> ")
                cinema.take_seats(choice_for_seats, choice_for_projection)
            cinema.print_reservation(choice_for_movie, choice_for_projection)
            final_command = input("Step 5 (Confirm - type 'finalize') >")
            for seat in cinema.all_seats:
                cinema.make_reservation(final_command,
                                        username_command,
                                        choice_for_projection,
                                        str(seat))

        command = input("Enter your choice: ")
        put = command.split(" ")

if __name__ == '__main__':
    main()