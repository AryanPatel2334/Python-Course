#Capitalize first letter of each word.

##text = "hare krishna"
##newtext = text.split()
##length = len(newtext)
##
##for i in range(length):
##    nt = newtext[i]
##    print(nt.capitalize(),end = " ")


text = "hare krishna"
capitalized = [word.capitalize() for word in text.split()]
print(" ".join(capitalized))


text = "hare krishna"
print(text.title())


