"""
File Name: highlow.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Practice loops with higher or lower math game
"""
#Import for random-int function: this will return an int between the two specified numbers
import random

#Establish variable outside of loop in order to get first play going
play = "yes"

while play.lower() == "yes":
    #Reset all numbers and counter for new game
    number = random.randint(1, 10)
    guess = 0
    guess_counter = 0

    #Actual gameplay loop
    while guess != number:
        guess = int(input("What is your guess? "))
        guess_counter += 1
        
        #If's to check values
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print("Correct!")
            print(f"This took {guess_counter} guesses.")
    play = input("Do you want to play again? (Yes/No) ")

print("Game over.")