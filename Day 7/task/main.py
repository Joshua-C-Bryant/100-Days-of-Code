import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create initial display with blanks
display = ""
for _ in chosen_word:
    display += "_"
print(display)

# TODO-1: Use a while loop to let the user guess again.
while "_" in display:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Keep previous correct letters.
    new_display = ""
    for index in range(len(chosen_word)):
        letter = chosen_word[index]

        if letter == guess:
            # Correct guess, reveal the letter
            new_display += letter
        else:
            # Keep the previous letter or underscore
            new_display += display[index]

    display = new_display
    print(display)

print("You guessed the word!")

