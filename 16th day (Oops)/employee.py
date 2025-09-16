class emp:
    def __init__(self,eno,ename):
        self.eno = eno
        self.ename = ename

    def show(self):
        print("EmployeeNo:",self.eno)
        print("EmployeeName:",self.ename)


e1 = emp(104,"Aryan")
e2 = emp(105,"Manav")
e3= emp(106,"Kaval")
e1.show()
e2.show()
e2.show()
