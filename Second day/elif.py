#if elif statements

print("Give score to Jiostar application")
print("Between 10 to 100")
score = int(input("Enter the score:"))
if score<=10 :
    print("Not like")
elif score>10 and score<=40 :
    print("Satisfied")
elif score>40 and score<=70 :
    print("Good")
else :
    print("Very nice")
    
