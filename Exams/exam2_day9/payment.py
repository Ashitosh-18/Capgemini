class Payment:
    def process_payment(self):
        print("Payment type ")

class CreditCard_Payment(Payment):
    def process_payment(self):
        super().process_payment()
        print("Credit Card")
        
class PayPal_Payment(Payment):
    def process_payment(self):
        super().process_payment()
        print("PayPal")

class Bitcoin_Payment(Payment):
    def process_payment(self):
        super().process_payment()
        print("Bitcoin")

res=CreditCard_Payment()
res1=PayPal_Payment()
res2=Bitcoin_Payment()

res.process_payment()
res1.process_payment()
res2.process_payment()