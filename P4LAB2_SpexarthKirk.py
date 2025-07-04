# Kirk Spexarth
# Friday, July 4, 2025
# P4LAB2
# Assignment tests student's knowledge of how to write code that displays information to users using loops.



run_again = "yes"

while run_again == "yes":  #THIS WILL REPEATE THE PROGRAM AS LONG AS YES IS TYPED. ( Also a while loop)
    user_input = input("Enter an integer: ")
    user_number = int(user_input)

    if user_number < 0:
        print("This program does not handle negative numbers.")  #If the integer the user entered is less than zero, the program should tell the user that it cannot accept negative values.

    else:
        for i in range(1, 13):  #this is the for loop
            print(f"{user_number} * {i} = {user_number * i}")

    run_again = input("\nWould you like to run the program again? ").lower() #  this will also convert the user's input to all lowercase letter. 


print("\nExiting program ...")
