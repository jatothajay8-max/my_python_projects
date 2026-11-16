class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Before updating marks ")
        print("Name : ",self.name)
        print("Marks : ",self.marks)

    def marks_update(self,insby):
        print("After updating marks ")
        print("Name : ",self.name)
        print("Marks : ",self.marks + insby)


c = Student('Ajay',80)
c.display()
print("______________\n")


c.marks_update(10)
