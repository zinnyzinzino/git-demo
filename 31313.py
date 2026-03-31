class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def get_price(self):
        return self._price
    def __str__(self):
        return f"product name : {self._name}, product price: {self._price}"
    

class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_product(self,item):
        self._items.append(item)
    def __add__(self,other):
        newcart = ShoppingCart()
        newcart._items = self._items + other._items
        return newcart

    def total(self):
        total = 0
        for i in self._items:
            total += i.get_price
        return total
    def __str__(self):
        return f"items: {self._items}"
    
class Discountedcart(ShoppingCart):
    def __init__(self, discountprecent):
        super().__init__()
        self._discountprecent=discountprecent
    def total(self):
        og = super().total_price
        discountamount = og * (self._discountprecent/100)
        return og - discountamount



class Employee:
    def __init__(self, name, id,):
        self._name = name
        self._id = id
    def calculate_salary(self):
        return 0

    def __str__(self):
        return f"{self._name} {self._id}"

class Fulltime(Employee):
    def __init__(self, name, id, monthlywage):
        super().__init__(name, id,)
        self._monthlywage = monthlywage
    def calculate_salary(self):
        return self._monthlywage
class Parttime(Employee):
    def __init__(self,name,id,hours,hourlypay):
        super().__init__(name, id)
        self._salary = hours * hourlypay
    def  calculate_salary(self):
        return self._salary
class Contractor(Employee):
    def __init__(self,name,id,contract_fee):
        super().__init__(name,id)
        self._contract_fee = contract_fee
    def calculate_salary(self):
        return self._contract_fee
class Team:
    def __init__(self):
        self.members = []
    def addtoteam(self, employee):
        self.members.append(employee)
    def __add__(self,other):
     if isinstance(other, Team):
            return Team(self.members + other.members)
     elif isinstance(other, Employee):
            return Team(self.members + [other])
     return NotImplemented
    def total_pay(self):
        total = 0
        for employee in self.members:
            total += employee.calculate_salary()

        return total
class Department:
    def __init__(self, name):
        self._name = name
        self.teams = []
    def addteam(self,team):
        self.teams.append(team)
    def total_payroll(self):
        total = 0
        for team in self.teams:
            total +=team.total_pay()
        return total
    
