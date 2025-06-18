# Kirk Spexarth
# June 18, 2025
# P2LAB2 - Car MPG Calculator
# This program stores car MPG data in a dictionary and calculates fuel usage based on user input.

cars = {

"Camaro": 18.21,
"Prius": 52.36,
"Model S": 110,
"Silverado": 26
}

keys = cars.keys()
print("Available vehicles:")
print(keys)


car_choice = input("Enter a vehicle to see it's mpg: ")
mpg = cars.get(car_choice)

print(f" \n The {car_choice} gets {mpg} mpg. \n ")

miles = float(input(f"How many miles will you drive the {car_choice}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {car_choice} {miles} miles.")

input("Press Enter to exit")