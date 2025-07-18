# Kirk Spexarth
# June 23, 2025
# P3HW1
# I am given a partial program with bugs.
# Below i have corrected the program


# I was supposed to put a comment here
# My Last Name
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))


# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total /len(grades)
print()
print(f"{'Results':-^40}")  # Centered title with dashes filling to width 40
print()
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average: {avg:.2f}")
print()
print(f"{'-':-^40}")  # Centered title with dashes filling to width 40
print()
# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

    # TO DO: finish this

input("Press Enter to exit")



