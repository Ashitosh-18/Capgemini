class customers:
    def __init__(self,customer_id,first_name,last_name,phone,email,location,zip_code):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.location=location
        self.zipcode=zip_code
        
    def display(self):
        print(f"enter customer id: {self.customer_id}\n first name: {self.first_name}\n last name: {self.last_name}\n phone:{self.phone}\n email:{self.email}\n location:{self.location}\n zip code:{self.location}")
        
class orders:
    def __init__(self,order_id,customer_id,order_status,order_date,required_date):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_status=order_status
        self.order_date=order_date
        self.required_date=required_date
        
    def display(self):
        print(f"enter order id: {self.order_id}\n enter customer id : {self.customer_id}\n order status: {self.order_status}\n order date:{self.order_date}\n required date:{self.required_date}")
        
def get_input():
    customer_id=input("Enter the customer id:")
    first_name=input("Enter the first name:")
    last_name=input("Enter the last name:")
    phone=input("Enter the phone number")
    email=input("Enter the email id")
    location=input("Enter the location of customer:")
    zip_code=input("Enter the zip code:")  
    
    return(customer_id,first_name,last_name,phone,email,location,zip_code)

res=customers
print(res.display())

def get_input():
    customer_id=input("Enter the customer id:")
    first_name=input("Enter the first name:")
    last_name=input("Enter the last name:")
    phone=input("Enter the phone number")
    email=input("Enter the email id")
    location=input("Enter the location of customer:")
    zip_code=input("Enter the zip code:")  
    
    return(customer_id,first_name,last_name,phone,email,location,zip_code)

customer_data=get_input()
res=customers(*customer_data)
res.display()
        
        
        
        
        

        