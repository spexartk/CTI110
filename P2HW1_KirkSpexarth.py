 # Kirk Spexarth

 # June 18, 2025

 # P2HW1

 # build on P1HW2 assignment . The only change we will be doing on P1HW2 is change how results are displayed
 
 
# Program Pseudocode (logic)
# 1. Ask the user to enter their total budget and store it in a variable.
# 2. Ask the user to enter their travel destination and store it in a variable.
# 3. Ask how much they will spend on gas and store it in a variable.
# 4. Ask how much they will spend on accommodation and store it in a variable.
# 5. Ask how much they will spend on food and store it in a variable.
# 6. Add up the gas, accommodation, and food expenses.
# 7. Subtract the total expenses from the budget to get the remaining balance.
# 8. Display all the expense information and the remaining balance


budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses


print()
print("------------Travel Expenses------------")
print("{:<20} {}".format("Location:", destination))
print("{:<20} ${:>8.2f}".format("Initial Budget:", budget))
print("{:<20} ${:>8.2f}".format("Fuel:", gas))
print("{:<20} ${:>8.2f}".format("Accommodation:", accommodation))
print("{:<20} ${:>8.2f}".format("Food:", food))
print("{:<20} ${:>8.2f}".format("Remaining Balance:", remaining_balance))
print("---------------------------------------")
print() 

# I needed some guidence on "{:<20} ${:>8.2f} but i now understand what it is doing and how it formats.
# Prompt the user to press Enter to keep the program window open,
# allowing them to view the output before it closes.
input("Press Enter to Exit...")