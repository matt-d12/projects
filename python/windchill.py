"""
File Name: windchill.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Calculate windchill from user inputs
"""
#This is to practice using functions to calculate wind chill
#Function for converting from Celsius to Fahrenheit as final output will be F
def c_to_f(degrees):
    return (degrees * 9/5) + 32

#Function to display wind chill from degrees in Fahrenheit
def wind_chill(degrees_f, wind_speed):
    return 35.74 + (0.6215 * degrees_f) - 35.75*(wind_speed ** 0.16) + ((0.4275 * degrees_f) * (wind_speed ** 0.16))

#Prompt user for temperature and unit
degrees = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")
#Convert unit to lowercase to avoid issues
unit = unit.lower()

#If statement to determine if we need to convert degrees from C to F
if unit == "c":
    degrees_f = c_to_f(degrees)
else:
    degrees_f = degrees

#Loop to print results, increments of 5 from 5-60 for the windspeed
for wind_speed in range(5, 65, 5):
    wind_temp = wind_chill(degrees_f, wind_speed)
    print(f"At temperature degrees {degrees_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_temp:.2f}F)")