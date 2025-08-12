"""
File Name: fluproject.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Practice pulling data from csv, cleaning up and caluclating results
"""
#Will be using data from reference_files/life-expectancy.csv
#Establish variables and lists - User values for inputted year stats
user_values = []
#Max values
max_life = -9999
max_country = "" 
max_year = 0
user_max_year = -9999
user_max_country = ""
#Min values
min_life = 9999
min_country = ""
min_year = 0
user_min_year = 9999
user_min_country = ""

user_year = int(input("\nEnter the year of interest: "))

with open("reference_files/life-expectancy.csv") as life_file:
    #Skip first line of CSV as these are just headers
    next(life_file)

    for line in life_file:
        #Cleanup data
        clean_line = line.strip()
        parts = clean_line.split(",")

        #Parts: Entity, Code, Year, Life expectancy(in years)
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        #Check max and min life expectancy for overall data
        if life > max_life:
            max_life = life
            max_country = country
            max_year = year
        if life < min_life:
            min_life = life
            min_country = country
            min_year = year

        #Check max and min for user's selected year
        if year == user_year:
            user_values.append(life)
            if life > user_max_year:
                user_max_year = life
                user_max_country = country
            if life < user_min_year:
                user_min_year = life
                user_min_country = country

#Calculate average after loop
average_life = sum(user_values) / len(user_values)

#Print all the results
print(f"\nThe overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")
print(f"\nFor the year {user_year}:")
print(f"The average life expectancy across all countries was {average_life:.2f}")
print(f"The max life expectancy was in {user_max_country} with {user_max_year:.2f}")
print(f"The min life expectancy was in {user_min_country} with {user_min_year:.2f}")
print()