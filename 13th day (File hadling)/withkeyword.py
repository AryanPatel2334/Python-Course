#Using with statement

with open("demo.txt") as file:
    data = file.read()
    print(data)
    
##with open("demo.txt","w") as file:
##    file.write("add by with statement")

##with open("demo.txt","a") as file:
##    file.write("\nAppended text.")
    
