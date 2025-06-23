# Kirk Spexarth
# June 23, 2025
# P3LAB
# This program calculates the most efficient way to break down a money amount
# into dollars, quarters, dimes, nickels, and pennies.

amount = float(input(" Enter amount as a float:"))
cents= int(round(amount * 100)) 
            
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

(input("-----Press Any key to end-----"))
