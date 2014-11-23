import ast
import datetime
from movies import Movie
from projections import Projection
from reservations import Reservation
from sqlalchemy import func


class Cinema():

    def __init__(self, session):
        self.__session = session

    def what_movie(self):
        self.lst = []
        self.movie_name = input("Enter name of movie: ")
        self.lst.append(self.movie_name)
        self.rating = input("Enter rating: ")
        self.lst.append(self.rating)
        return self.lst

    def add_movie(self):
        self.lst = self.what_movie()
        print("Adding new movie to the database via the session object")
        movie = Movie(name=self.lst[0], rating=self.lst[1])
        self.__session.add(movie)
        self.__session.commit()

    def show_movies(self):
        movies = self.__session.query(Movie).all()
        for movie in movies:
            print(movie)

    def add_projections(self):
        movie_id = input("Movie id: ")
        print("Adding new projection to the database via the session object")
        projection_date = self.time()
        projection = Projection(movie_type="3D",
                                date_time=projection_date,
                                movie_id=movie_id)
        self.__session.add(projection)
        self.__session.commit()

    def show_movie_projections(self, movie_id):
        self.select_title(movie_id)
        self.select_projections(movie_id)

    def select_title(self, movie_id):
        movie_name = self.__session.query(
            Movie).filter(Movie.id == movie_id).one()
        result = "Projections for " + movie_name.name
        return result

    def select_projections(self, movie_id):
        projections = self.__session.query(Projection).filter(
            Projection.movie_id == movie_id).group_by(
            Projection.date_time).all()
        for proj in projections:
            print(proj)

    def checking_movie_for_spots(self, movie_id):
        self.select_title(movie_id)
        projections = self.__session.query(
            Projection).filter(Projection.movie_id == movie_id).all()
        for proj in projections:
            print(str(proj.id) + ' - ' + str(
                proj.date_time) + ' (' + proj.movie_type + ') ' + str(
                self.take_spots(proj.id)) + " available spots")

    def take_spots(self, projection_id):
        self.spots = 100
        taken_spots = self.__session.query(
            func.count(Reservation.id)).filter(
            Reservation.projection_id == projection_id).all()
        self.spots -= taken_spots[0][0]
        return self.spots

    def print_seats(self):
        self.seats[0][0] = '  '

        for k in range(1, 11):
            self.seats[0][k] = str(k) + " "

        for k in range(1, 11):
            self.seats[k][0] = str(k) + " "
            if k == 10:
                self.seats[k][0] = str(k)

        for i in range(11):
            print("".join(str(x) for x in self.seats[i]))

    def check_seats_for_out_index(self, seats):
        seat = ast.literal_eval(seats)
        if seat[0] > 10 or seat[0] < 0 or seat[1] > 10 or seat[1] < 0:
            print("There is no seat like this one!")
            return False
        else:
            return True

    def show_seats(self, projection_id):
        seats = self.__session.query(
            Reservation.col, Reservation.col).filter(
            Reservation.projection_id == projection_id).all()

        self.seats = [[". " for x in range(11)] for x in range(11)]
        self.all_seats = []
        for seat in seats:
            self.seats[seat[0]][seat[1]] = 'x '
            self.spots -= 1
        self.print_seats()

    def check_seats_if_available(self, seats):
        place = ast.literal_eval(seats)
        if self.check_seats_for_out_index(seats) is True:
            if self.seats[place[0]][place[1]] == 'x ':
                print("This seat is taken!")
                return False
            else:
                return True

    def take_seats(self, seats, projection_id):
        #self.all_seats = []
        place = ast.literal_eval(seats)
        if self.seats[place[0]][place[1]] == ". ":
            self.seats[place[0]][place[1]] = "x "
            self.spots -= 1
            self.all_seats.append(place)

    def print_reservation(self, movie_id, projection_id):
        print("This is your reservation: ")
        movie = self.__session.query(
            Movie.name, Movie.rating).filter(
            Movie.id == movie_id).all()
        for col in movie:
            print("Movie: " + col.name + " (" + str(col.rating) + ")")

        projection = self.__session.query(
            Projection.date_time, Projection.movie_type).filter(
            Projection.id == projection_id).all()

        for col in projection:
            print("Date & time: " + str(col.date_time) + " (" + str(col.movie_type) + ")")

        seats = " "
        for seat in self.all_seats:
            seats += str(seat)
        print("Seats: " + seats)

    def make_reservation(self, final_command, username, projection_id, seats):
        place = ast.literal_eval(seats)
        if final_command.lower() == "finalize":
            reservation = Reservation(username=username,
                                      row=place[0],
                                      col=place[1],
                                      projection_id=projection_id)
            self.__session.add(reservation)
            self.__session.commit()

        self.all_seats = []

    def cancel_reservation(self, name):
        self.__session.query(Reservation).filter(
            Reservation.username == name).delete()
        self.__session.commit()

    def time(self):
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        hour = input("Hour: ")
        mins = input("Minutes: ")
        projection_date = datetime.datetime(year, month, day, hour, mins)
        return projection_date
