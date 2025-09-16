# Bank Statement

class bob:
    def __init__(self):
        print("BANK OF BARODA")
        self.balance = 50000

    def user(self):
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        if name == "aryan" and password == "1234":
            print(f"You are logged in. Welcome {name}")

            while True:
                print("\n-----------------")
                print("1. Credit your amount")
                print("2. Debit your amount")
                print("3. UPI Payment")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                print(f"Your Balance: Rs.{self.balance}")

                if choice == 1:
                    credit = int(input("Enter amount to credit: "))
                    if credit > 20000:
                        print("You cannot add more than 20000 at a time.")
                    elif credit < 0:
                        print("Enter only a positive value.")
                    else:
                        self.balance += credit
                        print(f"Rs.{credit} credited. New balance: Rs.{self.balance}")

                elif choice == 2:
                    debit = int(input("Enter amount to debit: "))
                    if debit > self.balance:
                        print("You do not have sufficient balance.")
                    elif debit < 0:
                        print("Enter only a positive value.")
                    else:
                        self.balance -= debit
                        print(f"Rs.{debit} debited. New balance: Rs.{self.balance}")

                elif choice == 3:
                    number = input("Enter 10-digit contact number: ")
                    if len(number) != 10 or not number.isdigit():
                        print("Please enter a valid 10-digit number.")
                    else:
                        debit = int(input("Enter amount to send: "))
                        pin = input("Enter your 4-digit PIN: ")
                        if len(pin) != 4 or not pin.isdigit():
                            print("Invalid PIN. Must be 4 digits.")
                        elif debit > self.balance:
                            print("You do not have sufficient balance.")
                        else:
                            self.balance -= debit
                            print(f"Rs.{debit} transferred to {number}. New balance: Rs.{self.balance}")

                elif choice == 4:
                    print("Thank you for using Bank of Baroda. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Login details are wrong")


# Create object and call user method
obj1 = bob()
obj1.user()
