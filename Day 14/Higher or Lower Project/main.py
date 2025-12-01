from art import logo, vs
from game_data import data
import random


def format_data(acc):
    return f"{acc['name']}, a {acc['description']}, from {acc['country']}"


def check_answer(guess, a, b):
    return (a > b and guess == "a") or (b > a and guess == "b")


print(logo)
score = 0
account_b = random.choice(data)

while True:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20, logo, sep="")

    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]

    if check_answer(guess, a_count, b_count):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break
