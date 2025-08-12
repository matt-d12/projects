"""
File Name: sentences.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose: To test out using multiple functions and generate sentences with three parts
"""
#Import random function to use when choosing words
import random

#Main function where we pass characteristics into make sentence function and print results
def main():
    sentence_one = make_sentence(1, "past")
    print(sentence_one)
    sentence_two = make_sentence(1, "present")
    print(sentence_two)
    sentence_three = make_sentence(1, "future")
    print(sentence_three)
    sentence_four = make_sentence(2, "past")
    print(sentence_four)
    sentence_five = make_sentence(2, "present")
    print(sentence_five)
    sentence_six = make_sentence(2, "future")
    print(sentence_six)

#Get random determiner based on quantity (single noun vs plural)
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose from word lists and return a determiner.
    word = random.choice(words)
    return word


#Determine whether noun is to be singular or plural
def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose noun from lists and return
    word = random.choice(words)
    return word

#Get verb based off quantity and tense from main
def get_verb(quantity, tense):
    #Lists of words depending on tense (future verbs just add will to base verbs)
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    base_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]    
    #If statemenets to determine which list to choose random word from
    if tense == "past":
        return random.choice(past_verbs)
    elif tense == "present":
        if quantity == 1:
            return random.choice(present_verbs)
        else:
            return random.choice(base_verbs)
    #Future verbs are the same as base verbs, they just add the word "will" in front
    elif tense == "future":
        return "will " + random.choice(base_verbs)
    
#Get a preposition based off word bank to be used in prepositional phrase
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

#Get a prepositional phrase made up to finish the second part of each sentence
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = str(f"{preposition} {determiner} {noun}")
    return prepositional_phrase

#Get an adjective from word bank
def get_adjective():
    adjectives = ["funny", "weird", "quiet", "loud", "big", "small", "happy", "sad"]
    adjective = random.choice(adjectives)
    return adjective

#Function to pass values into other get functions and return for main to print results
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase_one = get_prepositional_phrase(quantity)
    prepositional_phrase_two = get_prepositional_phrase(quantity)
    sentence = str.capitalize(f"{determiner} {adjective} {noun} {verb} {prepositional_phrase_one} {prepositional_phrase_two}.")
    return sentence

#Call main to execute code
main()