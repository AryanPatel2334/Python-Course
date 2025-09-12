#Remove duplicate character from the string

text = input("Enter string:")
result = ""
nt = text.lower()

for char in nt:
    if char not in result:
        result = result + char

print(result)
    
