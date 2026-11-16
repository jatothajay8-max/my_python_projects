class Library:
    name = "CMRCET LIBRARY"
    def __init__(self,name1,name2,name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        print(Library.name)
    def display(self):
        
        print("-----------\n")

        print("Books available ")
        print("1 ",self.name1)
        print("2 ",self.name2)
        print("3 ",self.name3)



        
v = Library('wings of fire','the legend','the rise')
v.display()

