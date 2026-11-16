# 26
class BankAccount:
    def __init__(self):
        self.balance = 1000
    def withdraw(self,amount):
        self.balance -= amount
        print("withdrawn by : ",amount)
    def credit(self,amount):
        self.balance += amount
        print("Credited by:  ",amount)
    def display(self):
        print("Bank Balance : ",self.balance)

print("Ajay's Account ")
c = BankAccount()
c.display()
c.withdraw(100)
c.display()
print("_________________\n")

print("Vijay's Account")
c1 = BankAccount()
c1.display()
c1.credit(1000)
c1.display()
