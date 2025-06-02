#Nested if
criteria = input("You are 12th pass or graduate:")
age = int(input("Enter your age:"))

if criteria == "graduate" :
    if age > 19 and age < 65 :
        print("Yes you are eligible")
    else :
        print("You are not eligible because your age is not matched..")
else :
    print("You are not eligible for the exam")
