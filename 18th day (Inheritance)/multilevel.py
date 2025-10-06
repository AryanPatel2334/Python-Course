#Multilevel inheritance

class A:
    def display1(self):
        print("I am class A")

class B(A):
    def display2(self):
        print("I am class B")

class C(B):
    def display3(self):
        print("I am class C")

c = C()
c.display1()
c.display2()
c.display3()

