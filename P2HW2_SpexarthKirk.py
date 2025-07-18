# Kirk Spexarth
# June 18, 2025
# P2HW2 - Grade Summary
# This program asks the user to enter grades for 6 modules,
# stores them in a descriptive list,
# then calculates and displays the lowest, highest, sum, and average of the grades,
# formatted exactly as required with spacing and two decimal places for average.



# Program Pseudocode:
# 1. Create an empty list named module_grades
# 2. Ask the user to enter grades for Module 1 through Module 6, one by one
# 3. Append each grade to the module_grades list
# 4. Calculate the lowest grade using min()
# 5. Calculate the highest grade using max()
# 6. Calculate the sum of grades using sum()
# 7. Calculate the average as sum divided by number of grades
# 8. Print a formatted header "Grades Summary" centered with dashes
# 9. Display the lowest, highest, sum, and average with proper spacing and average with two decimals



module_grades = []

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))


lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print()
print(f"{'Results':-^40}")  # Centered title with dashes filling to width 40
print()
print(f"{'Lowest Grade:':<20}{lowest:>10.2f}")
print(f"{'Highest Grade:':<20}{highest:>10.2f}")
print(f"{'Sum of Grades:':<20}{total:>10.2f}")
print(f"{'Average Grade:':<20}{average:>10.2f}")
#Added formating.
input("Press Enter to exit")