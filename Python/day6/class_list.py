class employee:
    def __init__(self,name,gender,dept,salary):
        self.name=name
        self.gender=gender
        self.dept=dept
        self.salary=salary
    def display(self):
        print(f"Name of the employee: {self.name}\n Gender: {self.gender}\n Department: {self.dept}\n Salary:{self.salary}\n")
def input_employee():
    name = input("Enter employee name:")
    gender = input("Enter employee gender: ")
    dept = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    return employee(name, gender, dept, salary)
employees=[]
num_employees = int(input("Number of employees: "))
if(num_employees<=0):
    print("No employees in the company")
    

for i in range(num_employees):
    print(f"Enter details for employee:")
    emp_inp = input_employee()
    employees.append(emp_inp)

print("\nEmployee Details:")
for emp_inp in employees:
    emp_inp.display()        

        
        