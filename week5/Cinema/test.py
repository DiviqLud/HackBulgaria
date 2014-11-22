#matrix = [[". " for x in range(11)] for x in range(11)]

#matrix[0][0] = '  '
#matrix[1][1] = 'x '

#for i in range(1, 11):
#    for j in range(1, 11):
#        if matrix[i][j] == "x ":
#            print("BLABL")

#for i in range(11):
#    print("".join(str(x) for x in matrix[i]))
import sqlite3

conn = sqlite3.connect("cinema.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

id = 1
username = "RadoRado"
projection_id = 1
row = 1
col = 2

#cursor.execute(''' INSERT INTO Reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)''', (username, projection_id, row, col))

#conn.commit()

#cursor.execute(''' DELETE FROM Reservations WHERE id = ''')

#conn.commit()

result = cursor.execute(''' SELECT * FROM Projections WHERE movie_id = 1''')

for row in result:
    print(row)

