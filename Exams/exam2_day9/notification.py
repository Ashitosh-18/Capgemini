class Notification:
    def send(self):
        print("Sending notification")

class Email_Notification(Notification):
    def send(self):
        super().send()
        print("Email sent")

class SMS_Notification(Notification):
    def send(self):
        super().send()
        print("SMS sent")

email=Email_Notification()
sms=SMS_Notification()

email.send()  
sms.send()  
