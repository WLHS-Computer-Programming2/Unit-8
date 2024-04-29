class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return f"Name: {self.name}\nID: {self.id}\nEmployee Type: {type(self).__name__}"

class SalaryEmployee(Employee):

    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
    def __str__(self):
        return super().__str__()+f"\nSalary: ${self.salary}"

    def weekly_pay(self)->float:
        return self.salary/52

class HourlyEmployee(Employee):

    def __init__(self,name,id,wage,max_hours):
        super(name,id)
        self.wage = wage
        self.max_hours = max_hours
    
    def __str__(self):
        return super().__str__()+f"\nWage: ${self.wage}\nMax Hours: {self.max_hours}"

    def weekly_pay(self,num_hours)->float:
        if num_hours > self.max_hours:
            return 40*self.wage + (num_hours - 40)*1.5*self.wage
        else:
            return 40*self.wage

class CommissionEmployee(SalaryEmployee):

    def __init__(self,name,id,salary,num_sales):
        super().__init__(name,id,salary)
        self.num_sales = num_sales
        self.commission = 100
    
    def __str__(self):
        return super().__str__()+f"\nNumber of Sales: {self.num_sales}"
    
    def weekly_pay(self):
        return self.salary/52 + self.commission * num_sales

e = Employee("Earl",7)
s = SalaryEmployee("Sally",34,95000)
c = CommissionEmployee("Carl",58,58000,40)
print(e)
print(s)
print(c)