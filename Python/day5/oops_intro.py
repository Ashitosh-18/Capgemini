class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def dispalay_info(self):
        print(f"this car is a {self.brand} and {self.model}")
        
c1=car('range rover','defender')
c2=car('audi','Q3')
c1.dispalay_info()
c2.dispalay_info()

# private constructor: ".__"
# protected constructor: "._"
# public or default: "."

