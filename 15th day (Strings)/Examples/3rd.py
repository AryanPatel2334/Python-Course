#String length

string = input("Enter a string:")
count = 0

for index, value in enumerate(string):
##    print(f"{index} {value}")
    count = index + 1
    print(count)
print("Length of string is:",count)
