class destructor_example:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
        
    def __del__(self):
        print(f"object {self.name} is destroyed")
        
obj=destructor_example("sample")
del obj