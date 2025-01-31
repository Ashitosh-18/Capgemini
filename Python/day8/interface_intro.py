from abc import ABC, abstractmethod
class Father(ABC):

	@abstractmethod					
	def disp(self):					# Abstract Method
		pass
		
#my = Father()						# Not possible to create object of a abstract class

class Child(Father):
	def disp(self):
		print("Child Class")
		print("Defining Abstract Method")

class Relative(Father):
	def disp(self):
		print("Rlative Class")
		print("Defining Rlative Method")
r = Relative()
c = Child()
c.disp()

# Mail ==> Interface
    # ==> send()  Abstract
# Email
# SMS
# WhatsAPP
