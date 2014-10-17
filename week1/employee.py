class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def weekly_pay():
        pass

    def get_name():
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def weeklyPay(self, hours):
        if hours <= 40:
            self.salary = hours * self.salary
        else:
            extra_hours = hours - 40
            extra_payment = 1.5*self.salary
            self.salary = 40 * self.salary
            self.salary += extra_hours * extra_payment
        return self.salary

    def getName(self):
        return self.name


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def weeklyPay(self, hours):
        self.salary = (self.salary // 12) // 4
        return self.salary

    def getName(self):
        return self.name


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        self.salary = (self.salary // 12) // 4
        self.bonus = 5*self.bonus
        self.salary += self.bonus
        return self.salary

    def getName(self):
        return self.name

staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
