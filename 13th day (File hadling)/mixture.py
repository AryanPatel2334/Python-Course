#Read, write and append
##
##file = open("demo.txt","w")
##file.write("This is demo file.")
##file.close()

##file = open("demo.txt","r")
##content = file.read()
##print(content)
##file.close()

##
##file = open("demo.txt","a")
##file.write("Appended text")
##file.close()


file = open("demo.txt","r")
for line in file:
    print(line.strip())
file.close()

