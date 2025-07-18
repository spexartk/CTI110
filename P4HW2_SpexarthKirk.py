# Kirk Spexarth

# Friday, July 4, 2025


# P4HW2 - Calculate gross pay for multiple employees

# Build on P3HW2 assignment. The program however will calculate gross pay for multiple employees, determined by user,
# And also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

### (Completed) I need to go back and fix so all forums of done are accepted. Ex. done, Done, DOne, doNE (Completed)

#Asks the user employee name
#Enter user pay rate and hours worked
#Calculate overpay and regular pay.
#Store these values in variables,
#Ask user to enter another employee's name to calculate salary for or "Done" to terminate program.
#Note we are using sentinels here.
#When user chooses to stop entering employee information ,
#display results
#THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name
#Display overtime total,
#Display regular pay total,
#Display gross pay total,
#Displaynumber of employees entered

#Pseudocode 
# uploade the needed code from p3hw2
# add the variable that stores the results.
# ask for the first employee's name.
#start the loop with paramiter employee_name is not = done.lower()  This allows all forms of done to be entered.
#calculate regular and overtime hours using P3H2
#calculate pay
#Print pay
#update company totals.
#ask for the next employee or to type done to finish.
#show the final totals after the loop ends. 

total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

employee_name = input("Enter employee's name (or type 'Done' to finish): ")
while employee_name.lower() != "done":
    
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

    print("\n--------------------------------------------------")
    print(f"Employee name:   {employee_name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}"
          f"{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
    print("-" * 85)
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}"
          f"${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<.2f}")

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    employee_name = input("\nEnter next employee's name (or type 'Done' to finish): ")

print("\nSummary of All Employees")
print("-" * 30)
print(f"Total number of employees entered: {employee_count}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")

input("\nPress Enter to exit")
