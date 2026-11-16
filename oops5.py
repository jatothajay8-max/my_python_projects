#make bank account class with deposit,withdraw and check balance

class Bankaccount :
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance :  ",self.__balance)

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

c1=Bankaccount()
c1.withdraw(500)
c1.show_balance()


print("-------------")


c2 = Bankaccount()
c2.deposit(1000)
c2.show_balance()
