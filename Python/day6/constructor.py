import dis
class example:
    static_variable=0
    def __init__(self):
        example.static_variable+=1
        print("this is a constructor")
        print("static variable value",example.static_variable)
        
obj1=example()
obj2=example()
obj3=example()

dis.dis(example)       
        