# Hangman
A simple game of hangman.

## Initial Concept:
Hangman involves one player pre-determining a word, and the other player having to guess the letters in the word. First challenge is going to be setting up a _literal_ dictionary to choose from.

### Progress: 11/23/2023
- Built the implementation. I have a dictionary constructed from all the unique words in the first 1000 lines of Mary Shelly's Frankenstein.
Current Features:
- Random selection of a word from the dictionary
- Display of blank spaces and correct guesses
- Win and lose states
- Limited number of incorrect guesses until loss

To-Do:
- Clean up the code. Put things into seperate methods to reduce the amount of logic in the main loop
- Scoring system? More unique letters -> Higher difficulty
- Score counts down. A perfect play would mean that there were no incorrect guesses.
- Leaderboard?
