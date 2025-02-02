class Vehicle:
    def display(self):
        return "This is a base class"
    
class Car(Vehicle):
    def display(self):
        print(super().display())
        return "Fortuner"
    
class Bike(Vehicle):
    def display(self):
        print(super().display())
        return "Royal Enfield"
    
class Electric_Car(Car):
    def display(self):
        print(super().display())
        return "Tesla"
    
res=Electric_Car()
print(res.display())

res1=Bike()
print(res1.display())