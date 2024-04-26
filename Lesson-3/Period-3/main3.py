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

e = Employee("Emily",1)
print(e)
s = SalaryEmployee("Sally",2,90000)
print(s)