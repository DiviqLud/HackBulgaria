import sqlite3

db = sqlite3.connect("create_company.db")
cursor = db.cursor()

result = cursor.execute("SELECT * FROM users")

for row in result:
    print(row)