import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

# TODO-1
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# Initial display
display = "_" * len(chosen_word)
print(display)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Rebuild the display every round
    new_display = ""
    for index in range(len(chosen_word)):
        letter = chosen_word[index]

        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    # TODO-2: Lose a life if wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong! You lose a life. Lives left: {lives}")
        if lives == 0:
            print("Game Over")
            game_over = True

    # Win check
    if "_" not in display:
        print("You win!")
        game_over = True

    # TODO-3: Show hangman stage
    print(stages[lives])

