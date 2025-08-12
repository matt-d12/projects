"""
File Name: mealprice.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Format inputs after calculations for a receipt
"""
#Gather inputs and convert
kid_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
kid_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

#Calculations
kid_total = (kid_meal * kid_count)
adult_total = (adult_meal * adult_count)
subtotal = kid_total + adult_total
tax = subtotal * (tax_rate / 100)
total = subtotal + tax

#Display results in a receipt format
#Use variable:.2f in f string to format only to 2 decimal places since dealing with money
#Use \t in f string to format display alignment 
print()
print("Your receipt is printed below:")
print("---------------------------------")
print(f"Qty\tItem\t\tPrice")
print(f"{kid_count}\tChild's meal\t${kid_total:.2f}")
print(f"{adult_count}\tAdult's meal\t${adult_total:.2f}")
print("---------------------------------")
print(f"Subtotal: \t\t${subtotal:.2f}" )
print(f"Sales Tax: \t\t${tax:.2f}")
print(f"Total: \t\t\t${total:.2f}")
print("---------------------------------")
print()

#Ask user for payment after they can see full receipt and display change owed
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change Due: ${change:.2f}")