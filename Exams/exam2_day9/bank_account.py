class BankAccount():
    def __init__(self,customer_name,balance=1000):
        self.cust_name=customer_name
        self.balance=balance
        
    def deposit(self,amt):
        if amt<=0:
            print("please enter a positive value")
            
        else:
            self.balance+=amt
            
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance")
            
        elif amt<=0:
            print("Please enter a positive value")
            
        else:
            self.balance-=amt
            
    def balance_amt(self):
        print(f"Account holder: {self.cust_name}\nasBalance: {self.balance}/-")
        
def get_input():
    customer_name=input("enter the name of account holder:")
        
    return customer_name

name=get_input()
res=BankAccount(name)

while True:
    print("1.Check balance:")
    print("2.Withdraw amount:")
    print("3.deposit amount:")
    print("4.Exit")
    
    val=int(input("Enter any one option:"))
    
    if val==1:
        res.balance_amt()
    
    if val==2:
        amt=int(input("enter the amount to withdraw: "))
        res.withdraw(amt)
        
    if val==3:
        amt=int(input("enter the amount to deposit: "))
        res.deposit(amt)
        
    ch=input("Do you want to continue y/n: ")
    if ch!='y':
        break
        