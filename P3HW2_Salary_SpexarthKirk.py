# Kirk Spexarth
# June 23, 2025
# P3HW2 - Salary Calculator
# This program asks the user for employee name, hours worked, and pay rate.
# It calculates pay for regular hours and overtime (if over 40 hours),
# and displays a formatted breakdown of all results.


## Program Pseudocode:
## 1. Ask user for employee name
## 2. Ask user for hours worked
## 3. Ask user for pay rate 
## 4. If hours worked > 40:
##  Calculate overtime hours = hours worked - 40
##  Set regular hours = 40
##  Else:
##  Overtime hours = 0
##  Regular hours = hours worked
## 5. Calculate regular pay = regular hours * pay rate
## 6. Calculate overtime pay = overtime hours * (pay rate * 1.5)
## 7. Calculate total pay = regular pay + overtime pay
## 8. Print separator line
## 9. Print employee name
## 10. Print column headers for the data
## 11. Print another separator line
## 12. Print all the calculated values neatly formatted

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked
    
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

print("--------------------------------------------------")
print(f"Employee name:   {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}"
      f"{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("-" * 85)

print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}"
      f"${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<.2f}")

input("\nPress Enter to exit")
