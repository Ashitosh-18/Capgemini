from abc import ABC,abstractmethod
class mail(ABC):
    @abstractmethod
    def send(self):
         pass
class email(mail):
    def send(self):
        print("this is an email")
class sms(mail):
    def send(self):
        print("this is an SMS")
class whatsapp(mail):
    def send(self):
        print("this is whatsapp message")
obj_1=email()
obj_2=sms()
obj_3=whatsapp()
obj_1.send()
obj_2.send()
obj_3.send()