class dog:
    def sound(self):
        print("meow")
        
class cat:
    def sound(self):
        print("bark")
        
for animal in [cat(),dog()]:
    animal.sound()
        
        