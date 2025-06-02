birthyear = int(input("Enter your birth year:"))
currentyear = int(input("Enter current year:"))
diff = currentyear - birthyear
print(diff)
if diff>=18 :
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
