#Reading from file

with open("f1.txt","r") as file:
    for line in file:
        print(line.strip())


