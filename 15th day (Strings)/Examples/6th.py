#String is palindrome or not

text = input("Enter a string:")
ntext = text.lower()
length = len(ntext)

rev_string = ""

for i in range(length - 1, -1, -1):
    rev_string += ntext[i]
print(f"Given string is {text} and reversed is {rev_string} ")


if rev_string == ntext:
    print("Palindrome")
else:
    print("Not palindrome")
                                    

     
