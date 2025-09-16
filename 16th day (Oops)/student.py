#Class and object

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:",self.name)
        print("Rollno:",self.roll)

#object creation

stud1 = Student("Pranav",101)
stud2 = Student("Aryan",102)
stud1.show()
stud2.show()
