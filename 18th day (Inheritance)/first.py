#Inheritance

class Parent:
    def speak(self):
        print("I am the parent")


class Child(Parent):  #child inherits from parent
    def play(self):
        print("I am playing")

#Using the classes

c = Child()
c.speak()  #inherits from parent
c.play()   #child's own method
