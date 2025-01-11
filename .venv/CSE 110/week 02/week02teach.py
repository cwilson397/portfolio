########################################################
# Programmer team: Colby
# ID card
# 5/1/2024
#########################################################


# defining main function
def main():
    # prompt for necessary values
    firstName = str(input("What is your First Name: "))
    lastName = str(input("What is your Last Name: "))
    emailAd = str(input("What is your Email: "))
    phoneNum = ''.join(filter(str.isdigit, input("What is your Phone Number: ")))
    jobTitle = str(input("What is your position title: "))
    idNum = ''.join(filter(str.isdigit, input("Enter your 7-digit ID Number: ")))
    hairCol = str(input("What is your hair color: "))
    eyeCol = str(input("What is your eye color: "))
    strMth = str(input("What month did you start in: "))
    train = bool(input("Have you completed the advanced training(yes or no)"))

    # processing phone and id number
    phoneNum2 = f"({phoneNum[:3]}) {phoneNum[3:6]}-{phoneNum[6:]}"
    idNum2 = f"{idNum[:2]}-{idNum[2:]}"

    # print out the user inputs
    print("Your ID Card is")
    print("----------------------------------------------------")
    print(lastName.upper()+",", firstName.capitalize())
    print(jobTitle.title())
    print("ID: ", idNum2)
    print()
    print(emailAd)
    print(phoneNum2)
    print()
    print(f"Hair: {hairCol.capitalize():<15} Eyes: {eyeCol.capitalize()}")
    print(f"Month: {strMth.capitalize():<14} Training: {train}")
    print("----------------------------------------------------")


# calling main function
main()
