import sqlite3

conn = sqlite3.connect("create_company.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

print('''List of commands that provides information about the company: 
         1. list_employees
         2. monthly_spending
         3. yearly_spending
         4. add_employee
         5. delete_employee <employee_id>
         6. update_employee <employee_id>
            ''')
command = input("Enter command> ")
lst = command.split(" ")
while lst[0] != "exit":
    if lst[0] == "list_employees":
        result = cursor.execute("SELECT id, name, position FROM users")
        for row in result:
            print(str(row['id']) + ' - ' + row['name'] + " - " + row['position'])
    if lst[0] == "monthly_spending":
        result = cursor.execute("SELECT monthly_salary FROM users")
        monthly_spending = 0
        for row in result:
            monthly_spending += int(row['monthly_salary'])
        print("The company is spending $" + str(monthly_spending) + "every month")
    if lst[0] == "yearly_spending":
        result = cursor.execute("SELECT monthly_salary, yearly_bonus FROM users")
        monthly_spending = 0
        bonuses = 0
        for row in result:
            monthly_spending += int(row['monthly_salary'])
            bonuses += int(row['yearly_bonus'])
        print("The company is spending $" + str(monthly_spending*12 + bonuses) + "every month")

    if lst[0] == "add_employee":
        name = input("Name of employee: ")
        monthly_salary = input("Monthly salary: ")
        yearly_bonus = input("Yearly bonus: ")
        position = input("Position: ")

        cursor.execute(''' INSERT INTO users(name,
                                     monthly_salary,
                                     yearly_bonus,
                                     position)
                VALUES(?, ?, ?, ?)''', (name, monthly_salary, yearly_bonus, position))
        conn.commit()

    if lst[0] == "delete_employee":
        user_id = lst[1]
        cursor.execute('''DELETE FROM users WHERE id = ? ''', (user_id))
        conn.commit()

    if lst[0] == "update_employee":
        user_id = lst[1]
        name = input("Name of employee: ")
        monthly_salary = input("Monthly salary: ")
        yearly_bonus = input("Yearly bonus: ")
        position = input("Position: ")

        cursor.execute('''UPDATE users
                          SET name = ?,
                              monthly_salary = ?,
                              yearly_bonus = ?,
                              position = ?
                          WHERE id = ?''', (name,
                                            monthly_salary,
                                            yearly_bonus,
                                            position,
                                            user_id))
        conn.commit()
    command = input("Enter command> ")
    lst = command.split(" ")
