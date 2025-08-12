"""
File Name: wordle.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Looping guesses with counter for popular Wordle game
"""
#Import random as going to use list of possible words
import random

#Variable to loop back through game process if playing again 
play = "yes"

while play.lower() == "yes":
    #Establish variables - Secret is randomly chosen from word bank
    word_bank = ["mosiah", "temple", "moroni", "dog", "computer"]
    secret = random.choice(word_bank)
    guess = ""
    guess_counter = 0
    #Hint based off length of chosen secret word
    hint = "_ " * len(secret)
    
    #Quick intro and show initial hint
    print()
    print("Welcome to the word guessing game!")
    print(f"Your hint is: {hint}")
    
    #Start game loop
    while guess.lower() != secret:
        guess = input("What is your guess? ")
        guess_counter += 1

        #Check if guess word is same length as secret
        if len(guess) != len(secret):
            print("Sorry, the guess must have the same number of letter as the secret word.")
            #Continue to skip rest of the loop and back to beginnng
            continue

        if guess == secret:
            print("\nCongratulations! You guessed it!")
            print(f"It took you {guess_counter} guesses to get the word {secret.upper()}.")
        else:
            print("Your guess was not correct.")
            #Update hint - will go through each letter guessed and check against actual word
            new_hint = ""
            for i in range(len(guess)):
                #Check if letter is in correct spot and make uppercase
                if guess[i] == secret[i]:
                    new_hint += guess[i].upper() + " "
                #Check if letter is in the word, but in wrong spot and make lowercase
                elif guess[i] in secret:
                    new_hint += guess[i] + " "
                #If letter is not in the word then put an underscore to show incorrect
                else:
                    new_hint += "_ "
            hint = new_hint
            print(f"\nYour hint is: {hint}")

#Once game over, ask to play again - if no, then loop will exit and print thank you statement
    play = input("Would you like to play again? (Yes/No) ")
print("\nThanks for playing!")