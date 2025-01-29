# single inheritance

class parent:
    def __init__(self):
        self.bigNose="7cm"
        
    def display_parent(self):
        print("this is the parent class")
        
class child(parent):
    def display_child(self):
        print("this is the child class")
        
parent_obj=parent()
child_obj=child()

# parent_obj.display_child()  # we cannot access child class from the parent class

parent_obj.display_parent()
child_obj.display_child()
child_obj.display_parent()

print(child_obj.bigNose)