class Calculator :
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!= 0:
            return a/b
        else :
            return "not divisible by  0  "
c1 = Calculator()
print(" Addition :  ",c1.add(1,1))

print("\n---------\n")
print("Substraction :  ",c1.substract(1,1))

print("\n---------\n")
print("Multiplication :  ",c1.multiply(1,1))

print("\n---------\n")
print("Division :  ",c1.divide(1,1))

