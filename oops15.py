class ShoppingCart:
    def __init__(self):
        self.items = []

    def additem(self,items):
        self.items.append(items)

    def display(self):
        print("shopping items are : ")

        for i in self.items:
            print(i)

c = ShoppingCart()
c.additem("  laptop")
c.additem("  mobile")
c.additem("  clothes")
c.display()
