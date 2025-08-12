"""
File Name: receipt.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose: To test out using dictionaries
"""
import csv
from datetime import datetime, timedelta
import sys
#Function to read the products.csv files
def read_products(filename):
    try:
        #Make empty dictionary
        product_dictionary = {}

        with open(filename, "rt") as product_file:
            reader = csv.reader(product_file)
            #Skip first row since header
            next(reader)

            for row in reader:
                product_number = row[0]
                product_name = row[1]
                product_price = float(row[2])
                product_dictionary[product_number] = [product_name, product_price]
        return product_dictionary
    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)
        return None

#Function to read the request.csv using product_dictionary
def process_request(filename, product_dictionary):
    try: 
        if product_dictionary is None:
            return None
        #Make list for shopping cart
        shopping_cart = []

        #Read request.csv for the shopping cart
        with open(filename, "rt") as request_file:
            reader = csv.reader(request_file)
            #Skip header row
            next(reader)
            for row in reader:
                product_number = row[0]
                product_quantity = int(row[1])
                product_name = product_dictionary[product_number][0]
                product_price = product_dictionary[product_number][1]
                #Add to shopping cart list
                shopping_cart.append([product_number, product_name, product_price, product_quantity])
        return shopping_cart
    #Add error exceptions
    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)
        return None
    except KeyError as error:
        print("Error: unknown product in the request.csv file")
        print(error)
        return None
    
#Function for shopping cart list
def print_receipt(shopping_cart):
    if shopping_cart is None or len(shopping_cart) == 0:
        return
    
    #Store name and variables
    store_name = "Inkom Emporium"
    print(f"{store_name}")
    print()
    subtotal = 0
    item_count = 0

    # Print individual items in shopping cart
    for item in shopping_cart:
        product_name = item[1]
        product_price = item[2]
        product_quantity = item[3]
        
        item_total = product_price * product_quantity
        subtotal += item_total
        item_count += product_quantity
        
        print(f"{product_name}: {product_quantity} @ {product_price}")

    #Summary of receipt
    print(f"\nNumber of Items: {item_count}")
    print(f"Subtotal: {subtotal:.2f}")
    #Calculate sales tax (6%)
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    print(f"Sales Tax: {sales_tax:.2f}")
    # Calculate and print total
    total = subtotal + sales_tax
    print(f"Total: {total:.2f}")
    print()
    #Thank you message
    print("Thank you for shopping at the Inkom Emporium.")
    #Print the current date and time
    current_datetime = datetime.now()
    print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))
    #Add return policy for 7 days from purchase
    return_date = current_datetime + timedelta(days=7)
    print(f"Return by: {return_date.strftime('%a %b %d %Y')}")


#Main function to call other functions and print errors if cannot find csv's
def main():
    try:
        product_dictionary = read_products("reference_files/products.csv")
        if product_dictionary is None:
            return
        
        shopping_cart = process_request("reference_files/request.csv", product_dictionary)
        if shopping_cart is None:
            return
        
        #Print receipt
        print_receipt(shopping_cart)

    except Exception as error:
        print(f"An unexpected error occured: {error}")

#Call main to run program
if __name__ == "__main__":
    main()