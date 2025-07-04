# Kirk Spexarth
# Friday, July 4, 2025
# P4HW1
# Assignment assess student ability to edit and enhance exiting programs
# program will use a loop. to calculate an average. after displaying score average (after dropping lowest score) , the program is to display a letter grade for the calculated average.



# first we need to define the begining of the function that takes the avg.
# this uses a series of if-elif-else statements.

def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# make a loop so you can keep using the program over and over. It is important to remember while in a loop the indentions needed.
repeat = "yes"
# Repeat the entire program as long as the user says "yes"
while repeat.lower() == "yes":
# Next we will ask how many scores need to be entered. and create a list to store them.

    num_scores = int(input("How many scores would you like to enter? "))

    valid_scores = []

#create a loop inside the loop that repeats exactly how many times you entereed for num_scores

    for i in range(num_scores):
        valid = False
        while not valid:  # This is important. Will repeat as long as valid is false. This makes sure we dont get stuck in an infinite loop.
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                valid_scores.append(score)  #this will add it to the list!
                valid = True #Setting valid to True causes the "while not valid loop" to stop running for this score.
            else:
                print("Invalid score. Please enter a score between 0 and 100.")

# next we need to use the information we have gathered in the table to display the results.
# must remember to add a variable for the lowest score and have it removed.



    lowest_score = min(valid_scores)

    modified_scores = valid_scores.copy()
    modified_scores.remove(lowest_score)

    average_score = sum(modified_scores) / len(modified_scores)

    letter_grade = get_letter_grade(average_score)
#now we must print our results. 
    print("\n" + "-" * 40)
    print(f"{'Results':^40}")
    print("-" * 40)
    print(f"Lowest score entered: {lowest_score:.2f}")
    print(f"Scores after dropping lowest score: {modified_scores}")
    print(f"Average of remaining scores: {average_score:.2f}")
    print(f"Letter grade: {letter_grade}")
    print("-" * 40)
# ask if you need to check another set of grades. If yes the program restarts. Also forceing lowercase.
    repeat = input("Do you want to check another set of grades? (yes/no): ").lower()
    
print("Thank you for trying my program.")
