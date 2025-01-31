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
        