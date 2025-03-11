##############################
# Receipt.py
# Colby Wilson
# CSE 111
# 3/3/2025
##############################


import csv
import random
import os

# Function to read products CSV file and return a dictionary
def read_dictionary(filename, key_column_index):
    products_dict = {}

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                if len(row) >= 3:
                    key = row[key_column_index]
                    value = [row[0], row[1], float(row[2])]
                    products_dict[key] = value
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        exit()
    
    return products_dict

# Function to print survey invitation
def print_survey_invitation():
    print("\n--- Customer Survey ---")
    print("We value your feedback! Please take a moment to complete our online survey.")
    print("Visit: www.example.com/survey\n")

# Function to print a coupon for a randomly chosen ordered item
def print_coupon(order_items):
    if order_items:
        selected_item = random.choice(order_items)
        product_name = selected_item[0]
        product_price = selected_item[1]
        print("\n--- Special Coupon ---")
        print(f"Save 10% on {product_name}!")
        print(f"Coupon valid for: ${product_price * 0.10:.2f} off your next purchase of {product_name}.\n")
    else:
        print("\nNo products ordered. No coupon available.\n")

def main():
    filename = "products.csv"
    request_filename = "request.csv"
    
    try:
        products_dict = read_dictionary(filename, 0)
        print("Product Dictionary:", products_dict)  # Debugging line

        order_items = []  # List to hold ordered items

        with open(request_filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            print("\nRequested Items:")
            for row in reader:
                if len(row) >= 2:
                    product_number = row[0]
                    quantity = int(row[1])

                    if product_number in products_dict:
                        product_name = products_dict[product_number][1]
                        product_price = products_dict[product_number][2]

                        # Add ordered item to the order_items list
                        order_items.append([product_name, product_price])

                        print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
                    else:
                        print(f"Product {product_number} not found.")

        # Print coupon for a product in the order
        print_coupon(order_items)

        # Print the survey invitation
        print_survey_invitation()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Missing product in dictionary: {e}")

if __name__ == "__main__":
    main()
