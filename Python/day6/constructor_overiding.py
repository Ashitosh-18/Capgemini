class myclass:
    
    def __init__(self,name):
        # print("this is my constructor")
        print(f"the name of the constructor is {name}")
        
    def __init__(self,age):
        print(f"the age of the constructor is {age}")
        
obj_1=myclass('abc')

# if we give more than one constructor in one class 
# then the first constructor will be over ride by the new given constructor
