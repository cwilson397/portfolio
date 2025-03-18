import csv

# Indexes for the CSV columns
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def read_compound_list(filename):
    """Read the CSV file into a list of lists."""
    compound_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            compound_list.append(row)
    return compound_list

def print_list(student_list):
    """Print each element of the list on a separate line."""
    for student in student_list:
        print(student)

def main():
    # Read the pupils.csv file into a list
    students_list = read_compound_list('.venv\CSE 111\week 11\pupils.csv')

    # ✅ Core Requirement: Sort by birthdate (oldest to youngest)
    students_list.sort(key=lambda student: student[BIRTHDATE_INDEX])

    print("\nSorted by birthdate (oldest to youngest):")
    print_list(students_list)

    # 🌟 Stretch Challenge 1: Sort by given name
    students_list.sort(key=lambda student: student[GIVEN_NAME_INDEX])

    print("\nSorted by given name:")
    print_list(students_list)

    # 🌟 Stretch Challenge 2: Sort by birth month and day (ignoring the year)
    students_list.sort(key=lambda student: (
        int(student[BIRTHDATE_INDEX][5:7]),  # Month
        int(student[BIRTHDATE_INDEX][8:10])  # Day
    ))

    print("\nSorted by birth month and day:")
    print_list(students_list)

# Call the main function
if __name__ == "__main__":
    main()
