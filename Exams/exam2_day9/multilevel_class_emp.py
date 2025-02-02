class Person:
    def disp(self):
        return "this is person class"
    
class Employee(Person):
    def disp(self):
        return "this is employee class"
    
class Manager(Employee):
    def approve_leave(self, employee_name):
        employee_name=input("Enter the employee name:")
        return f"{employee_name}'s leave approved."
    
res=Manager()
print(res.approve_leave(Employee))
print(res.disp())