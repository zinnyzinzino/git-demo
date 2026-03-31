class Employee:
    def __add__(self, other):
        return Team([self, other])

    def calculate_salary(self):
        raise NotImplementedError("need subclasses")


class Fulltimeemployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class Parttimeemployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


class Contractor(Employee):
    def __init__(self, name, project_fee):
        self.name = name
        self.project_fee = project_fee

    def calculate_salary(self):
        return self.project_fee


class Team:
    def __init__(self, employees):
        self.employees = employees

    def calculate_salary(self):
        total = 0
        for emp in self.employees:
            total += emp.calculate_salary()
        return total

    def __add__(self, other):
        if isinstance(other, Employee):
            return Team(self.employees + [other])
        if isinstance(other, Team):
            return Team(self.employees + other.employees)


class Department:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def total_payroll(self):
        total = 0
        for team in self.teams:
            total += team.calculate_salary()
        return total


e1 = Fulltimeemployee("Alice", 4000)
e2 = Parttimeemployee("Bob", 20, 80)
e3 = Contractor("Charlie", 3000)
e4 = Parttimeemployee("Diana", 25, 60)

team1 = e1 + e2
team1 = team1 + e3

team2 = e3 + e4

big_team = team1 + team2

print(e1.calculate_salary())
print(team1.calculate_salary())
print(big_team.calculate_salary())

department = Department()
department.add_team(team1)
department.add_team(team2)

print(department.total_payroll())