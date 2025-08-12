"""
File Name: shoppingcart.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Practice using multiple functions to edit lists via shopping cart interface
"""
#Declare lists and variables
items = []
prices = []
new_item = ""
new_price = 0
remove_number = 0
#Variable to indicate what user is wanting to do (Numbers 1-5)
menu_control = 0

#Function for option 1 - Add item
def add_item():
    new_item = input("What item would you like to add? ")
        #If to check that we don't include exit as an item 
    if new_item != "exit":
        #Add to the items list
        items.append(new_item)
        #Ask for price and add to the prices list
        new_price = float(input(f"What is the price of {new_item}? "))
        prices.append(new_price)
        #Confirm adding to cart for user
        print(f"{new_item.upper()} has been added to the cart.")
        menu()
    else:
        menu()

#Function for option 2 - View cart
def view_cart():
    #Extra formatting so it outputs as an easier to read table
    print("\nYour cart: ")
    print("-" * 40)
    #Formatting with 5 wide space for number, 20 for item name, 10 for price
    print(f"{'Number':<10} {'Item':<25} {'Price':<10}")
    print("-" * 40)
    #i to count which item in the lists and item for the name
    for i, item in enumerate(items):
        print(f"{(i+1):<10} {item:<25} ${prices[i]:<10.2f}")
    #No menu inside this function as using in remove_item function. Put in menu function though so works the same

#Function for option 3 - Remove item
def remove_item():
    #Check to make sure there are things in the cart first
    if len(items) != 0:
        #Show cart for ease of use
        view_cart()
        #Get number input to remove an item
        remove_number = int(input("\nWhich item would you like to remove? "))
        #Loop to remove item based on a number they enter and throw invalid for wrong number
        #Check their entry is between 1 and however long the item list is
        if 1 <= remove_number <= len(items):
            #Using pop function to remove the item and then tell user what they removed
            item_removed = items.pop(remove_number - 1)
            price_removed = prices.pop(remove_number - 1)
            print(f"{item_removed} for ${price_removed:.2f} was removed from the cart.")
        else:
            print("Invalid item number. Please enter the number of an item in your cart.")
    else:
        print("There are no items in the cart.")
    menu()

#Function for option 4 - Compute total
def compute_total():
    total = sum(prices)
    print(f"The total is ${total:.2f}")
    menu()

#Function for menu system
def menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    menu_control = int(input("Please enter an action: "))
    #If statment to check for valid inputs and decide which function to call next
    if menu_control == 1:
        add_item()
    elif menu_control == 2:
        view_cart()
        #Go back to menu since no menu in view_cart function as we use this in remove_item
        menu()
    elif menu_control == 3:
        remove_item()
    elif menu_control == 4:
        compute_total()
    #Option 5 is to quit program so just put in here as doesn't need a defined function
    elif menu_control == 5:
        print("Thank you. Goodbye.")
        quit
    else:
        print("Sorry this is not a valid number.")
        menu()

#Start program
print("Welcome to the Shopping Cart Program!")
menu()