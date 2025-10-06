#Usage of super() keyword

class parent:
    def show(self):
        print("I am parent")

class child(parent):
    def show(self):
        super().show()  #Call parent's show method
        print("I am child")

c = child()
c.show()



