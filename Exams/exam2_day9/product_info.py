class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def check_availability(self,quantity):
        if self.stock>=quantity:
            print(f"Requested quantity of {self.name} is available")
        
        else:
            print(f"Reqested quantity of {self.name} is not available")
            
def get_input():
    name=input("Enter the name of product: ")
    price=int(input("Price: "))
    stock=int(input("Stock available: "))
    quantity=int(input("Enter the quantity you want to purchase: "))
    
    return (name,price,stock,quantity)

name,price,stock,quantity=get_input()
res=Product(name,price,stock)
res.check_availability(quantity)        