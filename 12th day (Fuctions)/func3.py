def sum(v1,v2):
    sum = v1 + v2
    print("sum is:",sum)

def sub(v1,v2):
    sub = v1 - v2
    print("subtration is:",sub)

def mul(v1,v2):
    sub = v1 * v2
    print("Multiplication is:",sub)

def div(v1,v2):
    sub = v1 / v2
    print("Division is:",sub)



print("Basic Calculation")
v1 = int(input("Enter first value:"))
v2 = int(input("Enter second value:"))
choice = input("What you want: +, -, *, / :")

if (choice == "+"):
    sum(v1,v2)
elif (choice == "-"):
    sub(v1,v2)
elif (choice == "*"):
    mul(v1,v2)
elif (choice == "/"):
    div(v1,v2)
else:
    print("Out of choice")




