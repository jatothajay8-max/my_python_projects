# creating a class of mobiles and printing the brand and price

class Mobile:
    def __init__(self,name,price):
        self.name = name
        self.price = price

c1 = Mobile('realme',10000)
print(c1.name)
print(c1.price)


print("-------------")


c2 = Mobile('vivo ',20000)
print(c2.name)
print(c2.price)

        
