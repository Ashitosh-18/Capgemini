class Electronics:
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print("This is a parent class electronics")

class Mobile_Device(Electronics):
    def display(self):
        print("This is a mobile device")

class Smart_Phone(Mobile_Device):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print("This is a smart phone")
        print(f"its name is {self.name}")

name=input("Enter the name of the phone:")
res=Smart_Phone(name)
res.display()