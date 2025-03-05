###################################################
# CSE Week 09 Team Activity
# Colby Wilson
# 3/3/2025
###################################################


import csv

# Reads the contents of the CSV file and returns it as a dictionary
def read_dictionary(filename, key_column_index=0):
    student_dict = {}

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) >= 2:
                key = row[key_column_index]
                value = row[1]
                student_dict[key] = value

    return student_dict

def clean_inumber(inumber):
    # removes dashes and validates format for Inumber
    cleaned = inumber.replace("-", "")

    if not cleaned.isdigit():
        print("Invalid I-Number")
        return None
    elif len(cleaned) < 9:
        print("Invalid I-Number: too few digits")
        return None
    elif len(cleaned) > 9:
        print("Invalid I-Number: Too many digits")
        return None
    
    return cleaned

def main():
    filename = "students.csv"
    students = read_dictionary(filename)

    user_input = input("Enter an I-Number (with or without dashes): ")
    inumber = clean_inumber(user_input)

    if inumber is None:
        return
    
    student_name = students.get(inumber, "No such student")
    print(student_name)

if __name__ == "__main__":
    main()