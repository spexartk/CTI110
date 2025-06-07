# Kirk Spexarth
# Saturday, June 7, 2025
# P1HW2
# This program asks the user for their travel budget. The estimated costs for gas,
# accommodation, and food. It calculates the total expenses and shows how much money
# will be left after the trip.

# Program Pseudocode (logic)
# 1. Ask the user to enter their total budget and store it in a variable.
# 2. Ask the user to enter their travel destination and store it in a variable.
# 3. Ask how much they will spend on gas and store it in a variable.
# 4. Ask how much they will spend on accommodation and store it in a variable.
# 5. Ask how much they will spend on food and store it in a variable.
# 6. Add up the gas, accommodation, and food expenses.
# 7. Subtract the total expenses from the budget to get the remaining balance.
# 8. Display all the expense information and the remaining balance

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print()
print("Travel Expenses")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)
print()
print()

input("Press Enter to Exit...")

# added input to keep the program open,
# otherwise it closes immediately and the Travel Expenses are not shown.
