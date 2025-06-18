# Kirk Spexarth
# 6/18/2025
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle using a user-provided radius.

import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")

input("Press Enter to exit")