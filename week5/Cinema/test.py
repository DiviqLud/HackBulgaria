import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

result = cursor.execute("SELECT * FROM Projections")
for row in result:
    print(row)
print("................")

results = cursor.execute("SELECT * FROM Movies")
for row in results:
    print(row)

print("................")
results = cursor.execute("SELECT * FROM Reservations")
for row in results:
    print(row)
