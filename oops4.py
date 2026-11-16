# finding the area and perimeter of rectangle


class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("Area : ",self.length*self.width)

    def perimeter(self):
        print("Perimeter : ",2*(self.length + self.width))

c1 = Rectangle(2,10)
c1.area()
c1.perimeter()

    
