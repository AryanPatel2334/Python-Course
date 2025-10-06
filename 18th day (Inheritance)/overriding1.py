class A:
    def lion(self):
        print("King of the jungle")

class B(A):
    def lion(self):
        super().lion()
        print("Great hunter")

b = B()
b.lion()
        
