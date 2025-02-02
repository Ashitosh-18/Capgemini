from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

    @abstractmethod
    def subtract(self,a,b):
        pass

    @abstractmethod
    def multiply(self,a,b):
        pass

    @abstractmethod
    def divide(self,a,b):
        pass

class BasicCalculator(ICalculator):
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b!=0:
            return a/b
        else:
            return "Cannot divide by zero"

cal = BasicCalculator()

print(cal.add(10,5))       
print(cal.subtract(10,5))  
print(cal.multiply(10,5))
print(cal.divide(10,5))  
