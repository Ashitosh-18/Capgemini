from abc import ABC,abstractmethod

class Father(ABC):
    
    @abstractmethod
    
    # abstract method (method without body)
    
    # which is needed to be implemented in child class 'only'
    def display(self):
        pass
    
    # concrete method (method with body)
    
    # method which is already implemented in abstract method is called concrete method
    def show(self):
        print("concrete method")
        
class Son(Father):
    def display(self):
        print("son is implementing the abstract method ")
        
class Daughter(Father):
    def display(self):
        print("daughter is implementing the abstract method ")

# creating objects and calling methods        
obj=Son()
obj.display() 
obj.show()

obj=Daughter()
obj.display() 
obj.show()