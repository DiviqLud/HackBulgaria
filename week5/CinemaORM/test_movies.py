import unittest
from sqlalchemy import create_engine
import base


class TestMovies(unittest.TestCase):

    def test_add_movie(self):
