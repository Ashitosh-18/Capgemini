class orders:
    def __init__(self,order_id,customer_id,order_status,order_date,required_date):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_status=order_status
        self.order_date=order_date
        self.required_date=required_date
        
    def display(self):
        print(f"enter order id: {self.order_id}\n enter customer id : {self.customer_id}\n order status: {self.order_status}\n order date:{self.order_date}\n required date:{self.required_date}")
        