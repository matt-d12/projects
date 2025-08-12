"""
File Name: wordgame.py
Author: Matt D.
Course: CSE 110 | BYU-Idaho
Purpose: Multiple inputs into a madlibs style word game
"""
#Get user inputs for story 
print("Welcome to my little Mad Libs word game. Please provide the following: ")
user_adj = input("An adjective: ")
user_adj_two = input("Another adjective: ")
user_animal = input("An animal: ")
user_animal_two = input("Another animal: ")
user_exclamation = input("An exclamation: ")
user_verb_one = input("A verb: ")
user_verb_two = input("Another verb: ")
user_verb_three = input("Another verb: ")
user_verb_four = input("One more verb: ")
user_noun = input("A noun: ")
#article variable to determine using a vs an by checking the first letter of a word
article = "an" if user_noun[0] in "aeiou" else "a"

#Format and display word game -think about adding numbers? 
print("Your Mad Libs story:")
print(f"""The other day, I was really in trouble. It all started when I saw a very
{user_adj.lower()} {user_animal.lower()} {user_verb_one.lower()} down the hallway. "{user_exclamation.capitalize()}!" I yelled. But all 
I could think to do was to {user_verb_two.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {user_verb_three.lower()}
right in front of my family. """)
#Add continuation
print(f"""My family looked at the {user_animal.lower()} with nothing but {user_adj_two.lower()}.
Before we knew it, the {user_animal.lower()} had stolen {article} {user_noun.lower()}! We tried
to stop it, but were distracted by the herd of {user_animal_two.lower()}s {user_verb_four.lower()}ing 
just to our right. We decided we would not come back to that zoo ever again.""")