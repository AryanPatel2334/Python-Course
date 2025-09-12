#Count vowels

name = "Aryan"
newname = name.lower()
print(newname)
count = 0
vowels = "aeiou"

for char in newname:
    if char in vowels:
        count+=1
print(f"Number of vowels is {count}")
    
