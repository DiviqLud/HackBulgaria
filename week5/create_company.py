import sqlite3

db = sqlite3.connect("create_company.db")

cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
                    name TEXT,
                    monthly_salary TEXT,
                    yearly_bonus TEXT,
                    position TEXT)''')
db.commit()

name = input("Name of employee: ")
monthly_salary = input("Monthly salary: ")
yearly_bonus = input("Yearly bonus: ")
position = input("Position: ")

cursor.execute(''' INSERT INTO users(name,
                                     monthly_salary,
                                     yearly_bonus,
                                     position)
                VALUES(?, ?, ?, ?)''', (name, monthly_salary, yearly_bonus, position))

db.commit()
print('Employee inserted')

