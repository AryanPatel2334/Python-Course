class animal():
    def __init__(self,name):
        self.name = name

    def print(self):
        print(self.name+" "+"is an animal")

a1 = animal("Lion")
a2 = animal("Tiger")
a1.print()
a2.print()
