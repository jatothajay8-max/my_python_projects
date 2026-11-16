# 25
class Employee:
    def __init__(self):
        self.balance = 30000
        
    def display(self):
        print("Your Salary :  ",self.balance)
        
    def increase(self,amount):
        self.balance += amount
        print("Salary increased by  ",amount)

c = Employee()
c.increase(5000)
c.display()
