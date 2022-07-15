import os
import bank
from datetime import datetime

def main():
    # Display current user path
    print(f"Programmer: {os.path.expanduser('~')}")
    # Display current date and time
    now = datetime.now()
    print(now.strftime("%B %d, %Y @ %X\n"))

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    user1 = bank.Bank(name, age, gender)

    keep_trying = True

    while (keep_trying):
        print("\nPlease Select Transaction:")
        print("\n1. Deposit Money")
        print("2. Windraw Money")
        print("3. View Balance")
        print("4. End Transaction\n")

        choice = int(input("Enter a number from menu selection: "))

        if choice == 4:
            print(f"Thank you for banking with us {name}.\n")
            keep_trying = False
        elif choice == 1:
            amount = int(input("Enter amount to deposit: "))
            user1.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            user1.withdraw(amount)
        elif choice == 3:
            user1.view_balance()
        else:
            print("Invalid Input.\n")

main()

