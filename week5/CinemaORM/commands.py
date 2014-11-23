from sqlalchemy import create_engine
from cinema import Cinema
from sqlalchemy.orm import Session
import base


def main():
    engine = create_engine("sqlite:///cinema.db")
    base.Base.metadata.create_all(engine)

    session = Session(bind=engine)

    cinema = Cinema(session)

    print_menu()
    command = input("Enter your choice: ")
    put = command.split(" ")

    while put[0] != "end":
        if put[0] == "add_movie" or put[0] == '1':
            cinema.add_movie()
        if put[0] == "show_movies" or put[0] == '2':
            cinema.show_movies()
        if put[0] == "add_projection" or put[0] == '3':
            cinema.add_projections()
        if put[0] == "show_movie_projections":
            cinema.show_movie_projections(put[1])
        if put[0] == "make_reservation" or put[0] == '5':
            #ENTER INFORMATION FOR USER
            try:
                #USER INFORMATION
                user_info = step_one(cinema)
                #CHOOSING MOVIE
                movie_choice = step_two(cinema)
                # CHOOSING PROJECTIONS
                projection_choice = step_three(cinema)
                # CHOOSING SEATS
                step_four(cinema, user_info, projection_choice, movie_choice)
                # FINALIZE
                step_five(cinema, user_info, projection_choice)
            except GiveUpError:
                print("You just give up the reservation!")
                print_menu()

        if put[0] == "cancel_reservation":
            cinema.cancel_reservation(put[1])
        if put[0] == "exit":
            break
        if put[0] == "help":
            cinema.print_menu()
        command = input("Enter your choice: ")
        put = command.split(" ")


def step_one(cinema):
    username_command = input("Step 1 (USER): Choose name> ")
    tickets = input("Step 1 (USER): Choose number of tickets> ")
    cinema.show_movies()
    give_up = input("You can give up if you want> ")
    give_up_command(give_up)
    return tickets, username_command


def step_two(cinema):
    choice_for_movie = input("Step 2 (Movie): Choose a movie> ")
    cinema.checking_movie_for_spots(choice_for_movie)
    give_up = input("You can give up if you want> ")
    give_up_command(give_up)
    return choice_for_movie


def step_three(cinema):
    choice_for_projection = input(
        "Step 3 (Projection): Choose a projection> ")
    cinema.show_seats(choice_for_projection)
    give_up = input("You can give up if you want> ")
    give_up_command(give_up)
    return choice_for_projection


def step_four(cinema, user_info, projection_choice, movie_choice):
    for ticket in range(1, int(user_info[0]) + 1):
        choice_for_seats = input(
            "Step 4 (Seats): Choose seat " + str(ticket) + "> ")
        while cinema.check_seats_for_out_index(
                choice_for_seats) is False or cinema.check_seats_if_available(
                choice_for_seats) is False:
            choice_for_seats = input(
                "Step 4 (Seats):Choose seat " + str(ticket) + "> ")
        cinema.take_seats(choice_for_seats, projection_choice)
    cinema.print_reservation(movie_choice, projection_choice)
    give_up = input("You can give up if you want> ")
    give_up_command(give_up)


def step_five(cinema, user_info, projection_choice):
    final_command = input("Step 5 (Confirm - type 'finalize') >")
    for seat in cinema.all_seats:
        cinema.make_reservation(final_command,
                                user_info[1],
                                projection_choice,
                                str(seat))


class GiveUpError(Exception):
    pass


def give_up_command(command):
    if command == 'give up' or command == 'yes':
        raise GiveUpError


def print_menu():
        print(''' Welcome to your cinema!
                  Here are the things you can do:
                        1. add_movie
                        2. show_movies
                        3. add_projection
                        4. show_movie_projections <movie_id>
                        5. make_reservation
                        6. cancel_reservation <name>
                        7. exit
                        8. help''')


if __name__ == '__main__':
    main()
