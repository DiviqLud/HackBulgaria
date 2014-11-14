import sqlite3
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


    def helping_func(self, cursor, string):
        Projections.select_title(cursor, string)
