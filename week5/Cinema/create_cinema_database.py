import sqlite3
from datetime import datetime


db = sqlite3.connect("cinema.db")
cursor = db.cursor()

cursor.execute('''PRAGMA foreign_key = ON''')

#CREATE TABLE FOR MOVIES
cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies
                                                        (id INTEGER PRIMARY KEY,
                                                        name TEXT,
                                                        rating REAL)''')
db.commit()

#CREATE TABLE FOR PROJECTIONS
cursor.execute('''  CREATE TABLE IF NOT EXISTS
                        Projections(id INTEGER PRIMARY KEY,
                        movie_id INTEGER,
                        movie_type TEXT,
                        date_time DATETIME,
                        FOREIGN KEY(movie_id) REFERENCES Movies(id))''')
db.commit()

#CREATE TABLE FOR RESERVATIONS
cursor.execute(''' CREATE TABLE IF NOT EXISTS
                        Reservations(id INTEGER PRIMARY KEY,
                        username TEXT,
                        projection_id INTEGER,
                        row INTEGER,
                        col INTEGER,
                        FOREIGN KEY (projection_id) REFERENCES Projections(movie_id))''')

db.commit()
