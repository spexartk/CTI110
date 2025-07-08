# Kirk Spexarth
# Tuesday, July 8, 2025
# P5LAB
# This program will simulate a customer using a self-checkout machine


#First tell python to import random module, this contains a bunch of tools for generating random numbers

import random

#Import our P3Lab to easily
#define a function and name it disperse_change, this takes one input parameter : amount
def disperse_change(amount):
    #Breaks down a float amount into dollars and coins.
    cents = int(round(amount * 100)) 

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(f"{dollars} dollars")

    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(f"{quarters} quarters")

    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(f"{dimes} dimes")

    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(f"{nickels} nickels")

    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(f"{pennies} pennies")

# Generate a random amount owed, then create a function that handles the main process for one checkout
def main():
    
    total = round(random.uniform(0.01, 100.00), 2)
    print(f"Total amount owed: ${total}")

    #Add a loop to keep the program running for if payment is invalid. Repeat until valid.
    payment = float(input("Enter the amount of cash you will put in: $"))
    while payment < total:
        print("Insufficient payment. Please try again.")
        payment = float(input("Enter the amount of cash you will put in: $"))

    change = round(payment - total, 2)
    print(f"Change owed: ${change}")
    disperse_change(change)
    

    
#allow the user to run the program again.

run_again = "yes"
while run_again.lower() == "yes":
    main()
    run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()

print("Goodbye!")


