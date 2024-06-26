# Small guessing number game from Python. The user needs to guess the
# number within the minimum number of guesses.
# Source: https://www.geeksforgeeks.org/number-guessing-game-in-python/

import random
import math

# Get user's input for lower bound and upper bound
lower = int(input("Please input the lower bound: "))
upper = int(input("Please input the upper bound: "))

# Calculate the minimum number of guesses
min_guess = int(math.log2(upper - lower + 1))
current_guess = 0

# Generate a random number
random_num = random.randrange(lower, upper)
print("\nYou have", min_guess, "attempts to guess the number.\n")

# While loop for repetitive guessing
while current_guess < min_guess:
    current_guess += 1

    # Get the user's guess1
    user_guess = int(input("\nYour guess: "))

    # Guess == Number (User guessed correctly)
    if (user_guess == random_num):
        print("Congratulations! You guessed it in", current_guess, "try.")
        break
    

    # Guess > Number
    if(user_guess > random_num):
        print("Try Again! You guessed too high")
    
    # Guess < Number
    elif (user_guess < random_num):
        print("Try Again! You guessed too small")
    
    print(f'Attempts left: {min_guess - current_guess}')


# User didn't guess the integer in the minimum number of guesses
if (current_guess >= min_guess):
    print(f'\nThe number is {random_num}')
    print("Better Luck Next Time!")
