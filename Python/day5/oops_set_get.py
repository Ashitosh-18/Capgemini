class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    def set_salary(self,salary):
        self._salary=salary
            
    def get_salary(self):
        return self._salary
    
    def gross_salary(self,allowances):
        return self._salary+allowances
    
    def total_salary(self,allowances,tax,pf):
        gross=self.gross_salary(allowances)
        return gross-(tax+pf)

name=input("enter the name :") 
sal=int(input(f"enter the basic salary of{name}:"))     
emp=Employee(name,sal)

print("salary before update is",emp.get_salary())

allo=int(input("enter the allowances"))
tax=int(input("enter the tax:"))
pf=int(input("enter the pf:"))

gross=emp.gross_salary(allo)
net_salary=emp.total_salary(allo,tax,pf)

# emp.set_salary(int(input("enter the salary to set:")))
# print("salary after update is",emp.get_salary())

print("net salary:",net_salary)