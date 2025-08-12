"""
File Name: tempconversion.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Short program to convert from F to C
"""
#Import math function for conversion formula
import math

#Gather input from user
degrees_f = float(input("What is the temperature in Fahrenheit? "))

#Convert and display result
degrees_c = (degrees_f - 32) * 5/9
print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")