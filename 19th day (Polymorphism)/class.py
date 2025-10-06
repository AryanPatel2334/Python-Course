#Different classes with the same method

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat(Car):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford","Mustang")
boat1 = Boat("lbiza","Touring 20")
plane1 = Plane("Boeing","747")

for name in (car1,boat1,plane1):
    name.move()
