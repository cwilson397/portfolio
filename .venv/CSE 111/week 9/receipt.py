#########################################
# Receipt.py
# Colby Wilson
# CSE 111
# 3/3/2025
#########################################

# important csv functions
import csv

# reads the content of a csv file into a compound dictionary
def read_dictionary(filename, key_column_index):
    products_dict = {}

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) >= 3:
                key = row[key_column_index]
                value = [row[0], row[1], float(row[2])]
                products_dict[key] = value

    return products_dict

def main():
    filename = "products.csv"
    products_dict = read_dictionary(filename, 0)
    print("Prodcut Dictionary:", products_dict) # debugging line

    # opens file and processes request
    request_filename = "request.csv"

    with open(request_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        print("\nRequested Items:")
        
        for row in reader:
            if len(row) >= 2:
                product_number = row[0]
                quantity = int(row[1])

                if product_number in products_dict:
                    product_name = products_dict[product_number][1]
                    product_price = products_dict[product_number][2]

                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
                else:
                    print(f"Product {product_number} not found.")

if __name__ == "__main__":
    main()
