# 1
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        
        

c = Student('ajay',18)
c.display()
