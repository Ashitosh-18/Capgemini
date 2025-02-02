from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def calculate_area(self,length,width):
        print(f"Area of Rectangle: {length*width}")

class Circle(IShape):
    def calculate_area(self,radius):
        print(f"Area of Circle: {3.14*radius*radius}")

rect=Rectangle()
circle=Circle()

rect.calculate_area(5,3)   
circle.calculate_area(7)  

 
