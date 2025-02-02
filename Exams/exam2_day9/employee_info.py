class employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.dept=department
        
    def display(self):
        print(f"Name of the employee: {self.name}\nID: {self.id}\nDepartment: {self.dept}\n")
        
def get_input():
    name=input("Enter the employee name:")
    id=input("Enter the employee ID:")
    department=input("Department of employee is:")
    
    return (name,id,department)

name,id,department=get_input()
emp=employee(name,id,department)
emp.display()