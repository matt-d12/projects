"""
File Name: velocity.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Calculate velocity and more complex equations
"""
#import math function
import math

print("Welcome to the velocity calculator. Please enter the following:")
print() 

#Get inputs and set variables
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter, etc.): "))
t = int(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Calculate values
c = (1 / 2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
v_terminal = math.sqrt(m * g / c)

#Display results
print()
print(f"The inner value of c is : {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
print(f"The terminal velocity is {v_terminal:.3f} m/s")