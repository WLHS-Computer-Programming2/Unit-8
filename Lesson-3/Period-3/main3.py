class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return f"Name: {self.name}\nID: {self.id}"

class SalaryEmployee(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
    def __str__(self):
        return super().__str__()+f"\nSalary: ${self.salary}"

class HourlyEmployee(Employee):
    def __init__(self,name,id,wage,max_hours):
        super().__init__(name,id)
        self.wage = wage
        self.max_hours = max_hours
    
    def __str__(self):
        return super().__str__()+f"\nWage: ${self.wage}\nMax Hours: {self.max_hours}"
e = Employee("Emily",1)
print(e)
s = SalaryEmployee("Sally",2,90000)
print(s)
h = HourlyEmployee("Hank",3,17.84,35)
print(h)