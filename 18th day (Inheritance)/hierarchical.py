#Hierarchical inheritance

class parent:
    def greet(self):
        print("Hello from parent")

class child1(parent):
    def func1(self):
        print("Child 1 function")

class child2(parent):
    def func2(self):
        print("Child 2 function")

c1 = child1()
c2 = child2()
c1.greet()
c2.greet()




