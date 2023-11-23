# -*- coding: utf-8 -*-
"""
Main
Created on Wed Nov 22 23:22:17 2023

@author: Lucas Finney
The main file for my Hangman game
"""
import random


# Import the word list
path = "Text/Dictionary.txt"
with open(path,'r') as dictionary:
    words = dictionary.read().splitlines() 

# Select a random word
word = random.choice(words)

# TESTING LINE: Print out the word
print(word)

#Find the length of the word
word_length = len(word)

# Initialize the game
'''
for i in range(word_length):
    print(f"{i+1}_ ", end='')
print()'''


# Initialize a dictionary of the letters in the word
# Note, treat letters in word as set, then copy those letters into dictionary
guess_tracker = {char: False for char in set(word)}
list(set(word))


# This clears the console
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix' in both)
    else:
        _ = os.system('clear')

# NOTE FOR LATER: Move this into its own file!
# Get input
def get_input():
    usrInput = input('Please enter a character:')[0]
    print(f'Your single character input was: {usrInput}')
    return usrInput
    
# Check if a letter is present in the word
def check_guess(guess, _word):
    if guess in set(_word):
        guess_tracker.update({guess: True})
        print(f"\'{guess}\' is in the word")
    else:
        player.tries -= 1
        print(f" \'{guess}\' is not in the word")
        print(f"{player.tries} tries remaining!")


class player:
    tries = 6


# Main Loop
while True:
    print(f"____{player.tries} tries remaining!____")
    
    #Note: Maybe make this its own method?
    # This is where we print out either the blank spaces or the correctly
    # guessed letters
    for char in word:
        if guess_tracker[char]==True:
            print(f"{char} ", end='') #print out the character if the value in the guess_tracker is True
        else:
            print("_ ", end='') # Print an underline if not
    print() # Print a new line            
        
    
    # For hangman, you usually have 6 wrong guesses?
    
    # This should simultaneously get the input and check it
    check_guess(get_input(),word)
    
    

    
    # Check if all values are True after each guess
    if all(guess_tracker.values()):
        print("Congratulations! You've guessed all the letters.")
        break  # This exits the loop
    
    if player.tries <= 0:
        print("You lose!")
        break
        
    input("Press enter to continue...")
    clear_console()
