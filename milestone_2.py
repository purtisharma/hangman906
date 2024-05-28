#Task 1: Define the list of possible words

word_list= 'banana', 'mango', 'leechi','grapes','apple'
print(word_list)

# Task 2: Choose random word from the list

import random
word= random.choice(word_list)
print(word)

# Task 3: Ask your user for an input

guess= input("Single letter: ")

# Task 4: Check input of the single letter

if  len(guess)==1 & guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
     