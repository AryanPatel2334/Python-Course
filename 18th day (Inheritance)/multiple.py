#Multiple Inheritance

class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A,B):  # Inherits from both A and B
    pass    

c = C()
c.showA()
c.showB()






