####################################################
# Programmer: Colby Wilson
# 6/21/2024
# description: a shopping cart menu program I have
# I started last week playing around with seperate functions
# so I really expanded that this week
####################################################

# Initialize empty lists for cart items and prices
cart = []
prices = []

# Function to display the menu options
def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add an item to the cart
def add_item(cart):
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    cart.append(item)
    prices.append(price)
    print(f"'{item}' has been added to the cart at ${price:.2f}.")

# Function to view the current contents of the cart
def view_cart(cart, prices):
    if cart:
        print("\nThe contents of the shopping cart are:")
        for i, (item, price) in enumerate(zip(cart, prices), 1):
            print(f"{i}. {item} - ${price:.2f}")
    else:
        print("Your cart is empty.")

# Function to remove an item from the cart
def remove_item(cart, prices):
    view_cart(cart, prices)
    if cart:
        index = int(input("Which item would you like to remove? ")) - 1
        if 0 <= index < len(cart):
            item_removed = cart.pop(index)
            price_removed = prices.pop(index)
            print(f"'{item_removed}' has been removed from the cart.")
        else:
            print("Invalid item number. Please select a valid item.")
    else:
        print("Your cart is empty. Nothing to remove.")

# Function to compute and display the total price of items in the cart
def compute_total(prices):
    total = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")

# Main function to control the flow of the program
def main():
    print("Welcome to the Shopping Cart Program!")
    choice = 0

    while choice != '5':
        display_menu()
        choice = input("Please enter an action: ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart, prices)
        elif choice == '3':
            remove_item(cart, prices)
        elif choice == '4':
            compute_total(prices)
        elif choice == '5':
            print("Thank you. Goodbye.")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()