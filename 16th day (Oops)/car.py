class car:
    def __init__(self,car_name,speed):
        self.car_name = car_name
        self.speed = speed

    def display(self):
        print("CarName:",self.car_name)
        print("CarSpeed:",self.speed)

c1 = car("Harrier","180km/h")
c1.display()
