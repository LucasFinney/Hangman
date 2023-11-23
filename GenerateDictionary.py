# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:51:27 2023

@author: Lucas Finney
Goal: Generate a dictionary for use in my Hangman game. I'm going to do this by
importing Mary Shelly's Frankenstein as .txt, then I'll write each unique word
to a new dictionary file
"""

def unique_words(string):
    words = string.split()
    unique = []
    for word in words:
        if words.count(word) == 1:
            unique.append(word)
    return unique

contents = ""

with open('Text/pg84.txt', 'r', encoding='utf-8-sig') as txt:
    for i in range(1000):
        contents+=txt.readline()

words = unique_words(contents)

# Removing non-alphabetic characters
clean_words = [word for word in words if word.isalpha()]

# If you want to remove duplicates and make all words lowercase
unique_words = set(word.lower() for word in clean_words)

print(len(unique_words))

with open('Text/Dictionary.txt','w') as output:
    for word in unique_words:
        output.write(word+'\n')