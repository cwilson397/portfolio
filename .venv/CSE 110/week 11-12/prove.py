################################################################################
# 
# Programmer: Colby Wilson
# Date: 7/2/2024
# Description: Taking data from the life-expectancy.csv file 
# I was tasked to create a program to answer various questions about the file
# 
#################################################################################

import csv

# Function to display the menu options
def display_menu():
    print("\nPlease select one of the following:")
    print("1. Load dataset")
    print("2. Find minimum and maximum life expectancy")
    print("3. Calculate average life expectancy for a year")
    print("4. Identify largest drop in life expectancy from one year to another")
    print("5. Life expectancy details for a country")
    print("6. Quit")

# Function to load the dataset
def load_dataset(file_path):
    dataset = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            for line in reader:
                dataset.append(line)
        print("Dataset loaded successfully.")
        return dataset
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        return None

# Function to find minimum and maximum life expectancy
def find_min_max_life_expectancy(dataset):
    if not dataset:
        print("Please load the dataset first.")
        return
    
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    country_min = ""
    country_max = ""
    year_min = ""
    year_max = ""

    for line in dataset:
        try:
            year = int(line[2])  # Assuming Year is in index 2
            life_expectancy = float(line[3])  # Assuming Life expectancy is in index 3
            country = line[0]  # Assuming Entity (Country) is in index 0

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                country_min = country
                year_min = year

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                country_max = country
                year_max = year
        except ValueError:
            continue  # Skip lines where year or life expectancy cannot be converted

    if country_min and country_max:
        print(f"\nMinimum life expectancy: {min_life_expectancy:.2f} years in {country_min} ({year_min})")
        print(f"Maximum life expectancy: {max_life_expectancy:.2f} years in {country_max} ({year_max})")
    else:
        print("No valid data found in the dataset.")


# Function to calculate average life expectancy for a given year
def calculate_average_life_expectancy(dataset):
    if not dataset:
        print("Please load the dataset first.")
        return
    
    year = int(input("Enter the year of interest: "))
    total_life_expectancy = 0
    count = 0

    for line in dataset:
        try:
            if int(line[2]) == year:  # Assuming Year is in index 2
                total_life_expectancy += float(line[3])  # Assuming Life expectancy is in index 3
                count += 1
        except ValueError:
            continue  # Skip lines where year or life expectancy cannot be converted

    if count > 0:
        average_life_expectancy = total_life_expectancy / count
        print(f"\nAverage life expectancy for {year}: {average_life_expectancy:.2f} years")
    else:
        print(f"No data found for the year {year}")

# function to identify the largest drop in life expectancy
def indentify_largest_drop(dataset):
    if not dataset:
        print("Please load the dataset first.")
        return

    largest_drop = float('-inf')
    drop_country = ""
    drop_year = ""

    previous_life_expectancy = None

    for line in dataset:
        try:
            year = int(line[2])
            life_expectancy = float(line[3])
            country = line[0]

            if previous_life_expectancy is not None:
                current_drop = previous_life_expectancy - life_expectancy
                if current_drop > largest_drop:
                    largest_drop = current_drop
                    drop_country = country
                    drop_year = year

            previous_life_expectancy = life_expectancy
        except ValueError:
            continue

    if largest_drop != float('-inf'):
        print(f"\nLargest drop in life expectancy: {largest_drop:.2f} years in {drop_country} ({drop_year})")
    else:
        print("No valid data found in the dataset.")

# function to get details for specific country
def life_expectancy_details_for_country(dataset):
    if not dataset:
        print("Please load the dataset first.")
        return
    
    country_name = input("Enter the name of the country: ")
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    total_life_expectancy = 0
    count = 0

    for line in dataset:
        try:
            if line[0].lower() == country_name.lower():  
                life_expectancy = float(line[3])  
                
                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy
                
                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy
                
                total_life_expectancy += life_expectancy
                count += 1
        except ValueError:
            continue  # Skip lines where life expectancy cannot be converted

    if count > 0:
        average_life_expectancy = total_life_expectancy / count
        print(f"\nLife expectancy details for {country_name}:")
        print(f"Minimum life expectancy: {min_life_expectancy:.2f} years")
        print(f"Maximum life expectancy: {max_life_expectancy:.2f} years")
        print(f"Average life expectancy: {average_life_expectancy:.2f} years")
    else:
        print(f"No data found for the country '{country_name}'")

# Main function to control the flow of the program
def main():
    file_path = r'C:\Users\jedic\Documents\wdd130 workspace\.venv\CSE 110\week 11-12\life-expectancy.csv'

    print("Welcome to the Life Expectancy Analysis Program!")
    choice = 0
    dataset = None

    while choice != '6':
        display_menu()
        choice = input("Please enter an action: ")

        if choice == '1':
            dataset = load_dataset(file_path)
        elif choice == '2':
            find_min_max_life_expectancy(dataset)
        elif choice == '3':
            calculate_average_life_expectancy(dataset)
        elif choice == '4':
            indentify_largest_drop(dataset)
        elif choice == '5':
            life_expectancy_details_for_country(dataset)
        elif choice == '6':
            print("Thank you. Goodbye.")
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()