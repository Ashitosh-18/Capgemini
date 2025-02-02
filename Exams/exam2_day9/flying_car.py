class Car:
    def move(self):
        print("This is a car")
        
class Airplane:
    def move(self):
        print("This is an airplane")
        
# inherits from both Car and Airplane 
class flying_car(Car,Airplane):
    def move(self):
        print("This is a flying car")
        
res=flying_car()
res.move()