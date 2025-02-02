class Animal:
    def speak(self):
        print(" This is a parent class")
        
class Dog(Animal):
    def speak(self):
        print("the Dog barks")
        
class Cat(Animal):
    def speak(self):
        print("the Cat meows")
        
res=Dog()
res1=Cat()
res.speak()
res1.speak()