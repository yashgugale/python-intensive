"""
Exercise 1: Guessing Game

Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
Too high
Too low
Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
"""

# Imports
import random


# Guessing game
def guessing_game():
    rand_num = random.randint(0, 100)
    while True:
        input_num = int(input("Guess a number between 0 and 100: "))
        if input_num < rand_num:
            print("Too low. Choose again")
        elif input_num > rand_num:
            print("Too high. Choose again")
        else:
            print("Right selection! The number is: ", rand_num)
            break


# Main execution
def main():
    """
    Guessing game
    """
    guessing_game()


if __name__ == "__main__":
    main()
