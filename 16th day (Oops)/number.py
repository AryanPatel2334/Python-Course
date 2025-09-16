class number:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def value(self):
        c = self.a + self.b
        print(c)

n1 = number(10,20)
n2 = number(20,20)
n1.value()
n2.value()

