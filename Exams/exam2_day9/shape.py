class Shape:
    def area(self):
        print("Calculate area")

class Square(Shape):
    def area(self,side):
        print(f"Area of square is: {side*side}")

class Triangle(Shape):
    def area(self,base,height):
        print(f"Area of triangle is: {0.5*base*height}")

s=Square()
t=Triangle()

s.area(4)    
t.area(5,6) 
