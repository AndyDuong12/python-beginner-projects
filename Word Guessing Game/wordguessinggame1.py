# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
# The user first has to input their names and then, will be asked to guess any alphabet. 
# If the random word contains that alphabet, it will be shown as the output(with correct placement) 
# else the program will ask you to guess another alphabet. 
# The user will be given 12 turns(which can be changed accordingly) to guess the complete word.
# Source: https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

import random

name = input("What is your name? ")
print(f'Good Luck! {name}')
print("Guess the characters")

# List of words
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Get a random word from the list, number of turns, and a 'guesses' variable
# to store the user guesses
random_word = random.choice(words)
turns = 12
guesses = ''

# While loop when the user has more than 0 turns
while turns > 0:
    guessed_correctly = 0   # Variable to check how many words are not guessed left
    
    for x in random_word:   # Loop through the random word
        if x in guesses:    # Check if the user guessed the word correctly
            print(x, end=" ")
        else:               # The user guessed incorrectly
            print("_", end=" ")
            guessed_correctly += 1  # +1 to 'guessed_correctly' for each unguessed character
        
    if guessed_correctly == 0:    # The user guessed all the characters in the word
        print(f'\nYou Won! The word is {random_word}')
        break

    user_guess = input("\nGuess a character: ")
    guesses += user_guess

    if user_guess not in random_word:   # Check if the character the user guessed is not in the word
        turns -= 1
        print(f'Wrong. You have {turns} turns left.')   # Reduce a turn

# The user failed to guess the word
if turns == 0:
    print(f'You Lost! The word is {random_word}')