import unittest
from base import Base
#from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cinema import Cinema
from movies import Movie
from projections import Projection
from reservations import Reservation
from datetime import datetime


engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)

session = Session(bind=engine)


class TestCinema(unittest.TestCase):
    def setUp(self):
        self.my_cinema = Cinema(session)

    def test_add_movie(self):
        #self.my_cinema.add_movie() add new movie
        movie = session.query(
            Movie.name, Movie.rating, Movie.id).filter(
            Movie.name == "Bad boys")
        self.assertEqual(movie[0][0], "Bad boys")
        self.assertEqual(movie[0][1], 7.1)
        self.assertEqual(movie[0][2], 3)

    def test_show_movies(self):
        #self.my_cinema.show_movies()
        movies = session.query(Movie.name).all()
        self.assertEqual(movies, [('The Hunger Games',), ('Die Hard',), ('Bad boys',)])

    #def test_what_movie(self): 
        #movie = self.my_cinema.what_movie()
        #self.assertEqual(movie, ['Wtf', '5.5'])

    def test_add_projections(self):
        #self.my_cinema.add_projections() #add one new projection
        projection = session.query(
            Projection.movie_type, Projection.date_time, Projection.movie_id).filter(
            Projection.movie_id == 3)
        self.assertEqual(projection[0][0], "3D")
        self.assertEqual(projection[0][1], datetime(2014, 11, 24, 21, 30))
        self.assertEqual(projection[0][2], 3)

    def test_select_title(self):
        self.assertEqual(self.my_cinema.select_title(2), "Projections for Die Hard")

    #def test_select_projections(self): # samo printva projekciite
    #    self.my_cinema.select_projections(2)

    #def test_show_projections(self): # samo printva projekciite
    #    self.my_cinema.show_movie_projections(2)

    def test_take_spots(self):
        self.assertEqual(self.my_cinema.take_spots(2), 97)

    def test_seats_for_out_if_index(self):
        self.assertFalse(self.my_cinema.check_seats_for_out_index('(2, 44)'))
        self.assertTrue(self.my_cinema.check_seats_for_out_index('(2, 3)'))

    def test_seats_if_are_available(self):
        self.my_cinema.take_spots(2)
        self.my_cinema.show_seats(2)
        self.assertTrue(self.my_cinema.check_seats_if_available("(1, 2)"))
        self.assertFalse(self.my_cinema.check_seats_if_available("(7, 7)"))

    def test_cancel_reservation(self): #works only once !
        #old_reservation = session.query(Reservation).all()
        #self.assertEqual(len(old_reservation), 6)
        self.my_cinema.cancel_reservation("Ivo")
        new_reservation = session.query(Reservation).all()
        self.assertEqual(len(new_reservation), 5)
if __name__ == '__main__':
    unittest.main()
