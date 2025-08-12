"""
File Name: loan.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Gather inputs and calculate if someone meets criteria for loan
"""
#Qualify for a loan
#Get inputs from user on a scale of 1-10
print("For the following, please enter a number 1-10 rating: ")
loan_amount = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
#Boolean variable to check at end
approval = False

#Check if loan amount >= 5
if loan_amount >= 5:
    if credit >= 7 and income >= 7:
        approval = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            approval = True
        else:
            approval = False
    else:
        approval = False
#Check if loan amount < 5
else:
    if credit < 4:
        approval = False
    else:
        if income >= 7 or down_payment >= 7:
            approval = True
        elif income >= 4 and down_payment >= 4:
            approval = True
        else: 
            approval = False

#Check and display final result after calculations
if approval:
    print("You are approved!")
else: 
    print("You have been denied.")