class man:
    def man_person(self):
        return "this is a man"
class woman:
    def woman_person(self):
        return "this is a woman"
    
class person(man,woman):
    def child(self):
        return "this is a child"
obj=person()
print(obj.man_person())
print(obj.woman_person())
print(obj.child())