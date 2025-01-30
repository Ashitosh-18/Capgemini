class Shape:
    def area(self):
        pass
class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
obj_1=circle(22)
obj_2=rectangle(3,4)
print("the area of the circle is: ",obj_1.area())
print("the area of the rectangle is: ",obj_2.area())