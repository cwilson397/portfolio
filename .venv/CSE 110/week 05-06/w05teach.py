#######################################################
# Grade Calculator
# 05/22/2024
# Colby Wilson
#######################################################


def main():
    # Get the grade percentage from the user
    grade_percentage = int(input("Enter your grade percentage: "))

    # Determine the letter grade
    if grade_percentage >= 90:
        letter = "A"
    elif grade_percentage >= 80:
        letter = "B"
    elif grade_percentage >= 70:
        letter = "C"
    elif grade_percentage >= 60:
        letter = "D"
    else:
        letter = "F"

    # Determine if the user passed the course
    if grade_percentage >= 70:
        passed = True
    else:
        passed = False

    # Add a "+" or "-" to the letter grade
    if letter != "F":  # F doesn't get a sign
        last_digit = grade_percentage % 10
        if last_digit >= 7:
            sign = "+"
        elif last_digit < 3:
            sign = "-"
        else:
            sign = ""
        # Handle the case for A+ (which doesn't exist, only A and A-)
        if letter == "A" and sign == "+":
            sign = ""
        else:
            sign = ""

    # Print the letter grade and the pass/fail message
    print(f"Your letter grade is: {letter}{sign}")
    if passed:
        print("Congratulations! You passed the course.")
    else:
        print("Unfortunately, you did not pass. Better luck next time!")