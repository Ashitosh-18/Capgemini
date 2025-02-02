class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def display(self):
        print(f"Student name: {self.name}\nRoll number: {self.roll_number}\n")
        
def get_input():
    name=input("Enter the Student name: ")
    roll_number=input("Enter the roll number: ")
    
    return (name,roll_number)

name,roll_number=get_input()
val=Student(name,roll_number)
val.display()


