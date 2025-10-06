#Mix example

class A:
    def showA(self):
        print("Class A Called")

class B():
    def showB(self):
        print("Class B Called")

class C(A,B):
    def showC(self):
        print("Class C Called")

class D(A):
    def showD(self):
        print("Class D Called")

class E(A):
    def showE(self):
        print("Class E called")

        
c = C()
d = D()
e = E()
c.showA()
c.showB()
c.showC()
d.showA()
e.showA()
