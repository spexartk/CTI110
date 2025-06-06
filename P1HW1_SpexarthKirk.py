# Your Name: Kirk Spexarth
# Date: June 6, 2025
# Assignment Name: P1LAB2
# Description: This program calculates simple exponents and a math expression using user input.

#1
print("---- Calculating Exponenets ----")
print()

base = int(input("Enter an integer as the base value: "))   
exponent = int(input("Enter an integer as the exponent: "))

#2
Exponent_calculation = base ** exponent           

#3

print(base, "raised to the power of", exponent, "is", Exponent_calculation, "!!")
print()

#4

print("---- Addition and Subtraction ----")
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

#6
Addition_and_Subtraction  = (num1 + num2) - num3

#6
print(num1, "+", num2, "-", num3, "is equal to", Addition_and_Subtraction)

input("Press Enter to exit...")

# I added this last input to keep the program open,
# because otherwise it closes immediately and the final equation is not visible.
