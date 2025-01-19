#########################################
# Wednesday January 15th, 2025
# Discount program
# Programmed by Group 10: Colby, Bernard
#########################################

# importing datetime
import datetime

# getting day of the week
def day_of_week():
    # Get the current day of the week from computer
    return datetime.datetime.now().strftime("%A")

    
# customer input on items
def customer_input():
    # initialize subtotal
    subtotal = 0.0

    # prompt
    print("Enter the price and quantity of each item. Enter 0 as price to finish.")
    
    while True:
        try:
            price = float(input("Price: $"))
            if price == 0:
                break
            quantity = int(input("Quantity: "))
            subtotal += price * quantity
            print(f"Current Subtotal: ${subtotal:.2f}")  # Display the running total
        except ValueError:
            print("Invalid Input. Please enter numeric values.")
            continue
    return subtotal    


# discount calculation
def calc_disc(subtotal, day):
    # calcualtes based on subtotal and day of the week
    if day in ["Tuesday", "Wednesday"]:
        if subtotal >= 50:
            return subtotal * 0.1
        else:
            return 0.0
    else:
        return 0.0
    
# Sales Tax (Idah has 6% sales tax)
def calc_salest(amount, tax_rate=0.06):
    # Calculates sales tax post discount
    return amount * tax_rate

# main function
def main():
    # call customer input()
    subtotal = customer_input()

    # call current day
    day = day_of_week()

    # calc discount
    discount = calc_disc(subtotal, day)
    disc_subtotal = subtotal - discount

    # calc sales tax
    sales_tax = calc_salest(disc_subtotal)

    # final total
    total = disc_subtotal + sales_tax

    # Printed results
    print("\nSummary:")
    if discount > 0:
        print(f"Discount: ${discount:.2f}")
    elif day in ["Tuesday", "Wednesday"]:
        print(f"You need to spend an additional ${50 - subtotal:.2f} to receive a discount.")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")  

#Run Main Function
main()