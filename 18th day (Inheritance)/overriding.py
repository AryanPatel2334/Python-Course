#Method overriding

class Parent:
    def speak(self):
        print("Parent speak")

class Child:
    def speak(self):  # overrides the parent method
        print("I am child")

c = Child()
c.speak()
