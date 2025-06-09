#combination of basics of python

eat = input("Are you hungry right now yes or no? :")

if eat == "yes":
    print("What will you eat?")
    items = ["Fruits","FastFood","Homemade"]
    for i in items:
        print(i)
    choice = input("Write here:")

    if choice == "Fruits":
        print("Which fruit?")
        fr = ["Apple","Banana","Mango","something else"]
        for i in fr:
            print("-",i)
        choice1 = input("Write here:")
        print("You want vitamins and proteins.")
    elif choice == "FastFood":
        print("Which fastfood?")
        ff = ["AlooPuri","Khaman","Frenki","something else"]
        for i in ff:
            print("-",i)
        choice2 = input("Write here:")
        print("Hmm nice.")
    elif choice == "Homemade":
        print("Which one?")
        hm = ["Dal-Chawal","Kari-Khichadi","Gujarati-Thali","something else"]
        for i in hm:
            print("-",i)
        choice1 = input("Write here:")
        print("Best choice forever.")
    else:
        print("You want something else")
else:
    print("Ok buddy.")
    time = int(input("how much time you eat in a day? 1,2?:"))
    if time == 1:
        print("Not enough buddy you have to eat at least 2 times.")
    elif time == 2:
        print("Good it is okk.")
    elif time == 3:
        print("You want to gain your weight")
    else:
        print("..You are foody man..")
print("Stay healthy Stay Happy  ❁´◡`❁")
   
    

        
