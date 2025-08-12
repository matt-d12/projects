"""
File Name: idbadge.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Get multiple inputs and format to a clean output
"""
#Get user info and store all inputs as variables
print("Hi there! Thank you for using the automated security ID badge program.")
print("Please answer the following questions as accurately as possible.")
first_name = input("What is your first name? ")
last_name = input("And what is your last name? ")
email = input("What is your email address? ")
phone = input("What is your phone number? ")
job_title = input("What is your job title? ")
id_number = input("What is your ID number? ")
hair = input("What is your hair color? ")
month = input("What is your birth month? ")
eyes = input("What is your eye color? ")
training = input("Have you completed your security training? (Yes/No) ")

#Post results in specific format regardless of input lengths
print("Your ID is printed below: ")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair:15} Eyes: {eyes}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------")