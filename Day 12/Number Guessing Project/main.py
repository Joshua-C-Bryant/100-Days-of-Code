import random

logo = r"""
 _____ _     _____ ____  ____    _____ _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __Y \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
| |  _| | |||  \  |    \|    \    / \ | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | | | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/ \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
"""


EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks guess vs answer and returns remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0

def set_difficulty():
    """Gets difficulty from user and returns number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = None

    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print("You've run out of guesses. You lose!")
            print(f"The number was {answer}.")
        elif guess != answer:
            print("Guess again.\n")

game()
