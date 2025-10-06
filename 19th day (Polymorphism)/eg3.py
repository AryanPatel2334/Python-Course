class jungle:
    def __init__(self,age):
        self.age = age

    def walk(self):
        print("Walk!")

class lion(jungle):
    pass

class monkey(jungle):
    def walk(self):
        print("Jump!")


class eagle(jungle):
    def walk(self):
        print("Fly!")


l1 = lion(20)
m1 = monkey(25)
e1 = eagle(40)

for i in (l1,m1,e1):
    i.walk()
