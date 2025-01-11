#######################################################################################
# Programmer: Colby Wilson
# Programming Date:
# Part One: 5/6/2024
# Program Name: POS Resturaunt.
# P1 Description: 
# Ask users for various variables and compute and display the result
# Part Two:
#########################################################################################


def main():

    # Recieving the inputs
    numChild = int(input("Enter the number of children in your party: "))
    numAdt = int(input("Enter the number of adults in your party: "))
    numApt = int(input("Enter the number of appetizers: "))
    numChildMeal = float(input("Enter the price of child meals: "))
    numAdtMeal  = float(input("Enter the price of adult meals: "))
    numAptMeal = float(input("Enter the price of an appetizer: "))
    saleTxPct = float(input("Enter the sales tax for your area: "))
    tipInt = int(input("Enter the desired tip percentage(15% = 1, 20% = 2, 25% = 3, 30% = 4, No tip = 0): "))
    paymenC = int(input("Enter 1. card or 2. cash : "))

    
    
    # Taking the tipInt and putting it as the decimal
    if tipInt == 1:
        tipPct = .15
    elif tipInt == 2:
        tipPct = .20
    elif tipInt == 3:
        tipPct = .25
    elif tipInt == 4:
        tipPct = .30
    else:
        tipPct = .00

    # progress checking
    print("Tip calculated")

    # sales tax checks if entered as X.XX rather than .XXXX
    if saleTxPct >=1:
        saleTxDec = (saleTxPct / 100)
    else:
        # already in decimal format
        saleTxDec = saleTxPct

    # progress checking
    print("Sales tax calculated.")

    # Calculating the subtotal
    totChld = numChild * numChildMeal
    totAdt = numAdt * numAdtMeal
    totApt = numApt * numAptMeal
    subtotal = totAdt + totApt + totChld
    subtotalTx = (saleTxDec * subtotal)

    # calculating the total
    totOvr = subtotalTx + subtotal


    # progress checking
    print("Subtotal calculated")

    # printing out itemized receipt 
    print(f"----------------------------------------------------------------")
    print(f"The appetizers ordered is {numApt}, that comes out to ${round(totApt,  2)}. ")
    print(f"The Adult meals ordered is {numAdt}, that comes out to ${round(totAdt, 2)}.")
    print(f"The Child meals orded is {numChild}, that comes out to ${round(totChld, 2)}")
    print()
    print(f"----------------------------------------------------------------")
    print(f"Your subtotal for the above is ${round(subtotal, 2)}")
    print(f"The sales tax is {saleTxDec} that comes out to ${round(subtotalTx, 2)}")
    print(f"Your Total is ${round(totOvr, 2)}")
    print(f"----------------------------------------------------------------")
    print()

    # Payment Calculator
    if paymenC == 1:
        payment = totOvr
    else: 
        payment = int(input("Enter the amount payed: "))

    # calcualtes change
    if payment > totOvr:
        change = float(payment - totOvr)
    else:
        change = float(0.00)

    print(f"Payment made is ${round(payment, 2)}")
    print(f"The change due is ${round(change, 2)}")
    print(f"----------------------------------------------------------------")


    



main()