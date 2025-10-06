#Example

class animal1:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is an animal")

class animal2(animal1):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is an animal")

class animal3(animal1):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is an animal")
        
a1 = animal1("Lion")
a2 = animal2("Monkey")
a3 = animal3("Eagle")

for a in (a1,a2,a3):
    a.walk()
