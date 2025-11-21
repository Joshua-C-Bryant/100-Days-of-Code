import random
from hangman_words import word_list          # TODO-1
from hangman_art import stages, logo         # TODO-2 & TODO-3

# Print the logo at the start of the game (TODO-3)
print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(f"Pssst... the answer is {chosen_word}")   # Remove later

# Create initial placeholder
display = ""
for _ in chosen_word:
    display += "_"

print("Word to guess: " + display)

game_over = False
correct_letters = []
guessed_letters = []     # <-- for TODO-4

while not game_over:

    # TODO-6: Tell the user how many lives they have
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    # TODO-4: Warn if the user already guessed the letter
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
    guessed_letters.append(guess)

    new_display = ""

    # Build updated display
    for i in range(len(chosen_word)):
        letter = chosen_word[i]

        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print("Word to guess: " + display)

    # TODO-5: Wrong guess → lose a life
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print("*********************** YOU LOSE **********************")
            print(f"The correct word was: {chosen_word}")  # TODO-7

    # Win condition
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # TODO-2: Print correct stage from hangman_art
    print(stages[lives])
