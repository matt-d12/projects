"""
File Name: tirevolume.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose: Calculate tire volume
"""
#import math as we are using pi as well as import date time to get info from user machine
import math
from datetime import datetime

#Variable to run initial program
run = "yes"

#Main function to get tire specs from user
def tire_specs():
    #Get date from system and convert to correct format
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d")
    #Get inputs from user 
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the tire in inches (ex 15): "))
    #Calculate volume of the tire
    volume = float((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000)
    print((f"\nThe approximate volume is {volume:.2f} liters."))

    #Open volumes file to store values
    with open("volumes.txt", "a") as volume_file:
        volume_file.write(f"{formatted_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

#Call function to run program and use loop to ask for multiple inputs
while run.lower() == "yes":
    tire_specs()
    run = input("\nWould you like to enter specs for another tire? (Yes/No) ")
