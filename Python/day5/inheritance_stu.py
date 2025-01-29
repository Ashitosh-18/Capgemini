class student:
    def __init__(self,name,age,school_name):
        self.name=name
        self.age=age
        self.school_name=school_name
        
    def display_stu(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"school name:{self.school_name}")
        
class UG_student(student):
    def __init__(self,name,age,school_name,college_name):
        super().__init__(name,age,school_name)
        self.college_name = college_name

    def display(self):
        super().display()
        print(f"College: {self.college_name}")

class PGStudent(UG_student):
    def __init__(self, name, age, school_name, college_name, pg_name):
        super().__init__(name, age, school_name, college_name)
        self.pg_name = pg_name

    def display(self):
        super().display()
        print(f"PG: {self.pg_name}")

# Creating an instance of PGStudent
student = PGStudent("Amit", 25, "ABC School", "XYZ College", "LMN University")

# Displaying the student's details
student.display()
        
        
        