import random
import os
import time

# -------------------------------
# ASCII ART CARD FUNCTIONS
# -------------------------------

def ascii_card(card):
    """
    Returns an ASCII representation of a card.
    """
    value = str(card.value)
    suit = card.suit

    # Formatting for left/right alignment
    if len(value) == 1:
        left = value + " " * 7
        right = " " * 7 + value
    else:
        left = value + " " * 6
        right = " " * 6 + value

    return [
        "┌─────────┐",
        f"│ {left}│",
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│ {right}│",
        "└─────────┘",
    ]


def ascii_back():
    """
    A hidden/face-down playing card.
    """
    return [
        "┌─────────┐",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "└─────────┘"
    ]


def print_cards(cards, hidden=False):
    """
    Print a row of ASCII cards.
    'hidden=True' hides all but the first card.
    """
    ascii_list = []

    for i, card in enumerate(cards):
        if hidden and i == 1:
            ascii_list.append(ascii_back())
        else:
            ascii_list.append(ascii_card(card))

    # Print row by row
    for line in range(7):
        print("  ".join(card[line] for card in ascii_list))


# -------------------------------
# OOP BLACKJACK CLASSES
# -------------------------------

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        suits = ["♠", "♥", "♦", "♣"]
        self.cards = [Card(v,s) for v in values for s in suits]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def value(self):
        total = 0
        aces = 0

        for c in self.cards:
            if c.value in ["J","Q","K"]:
                total += 10
            elif c.value == "A":
                total += 11
                aces += 1
            else:
                total += c.value

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total


class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add(deck.deal())


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")


# -------------------------------
# GAME ENGINE
# -------------------------------

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def clear(self):
        pass

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

    def show_hands(self, reveal_dealer=False):
        print("\n==========================")
        print("       BLACKJACK")
        print("==========================\n")

        print(f"Dealer's Hand:")
        if reveal_dealer:
            print_cards(self.dealer.hand.cards)
            print(f"Value: {self.dealer.hand.value()}")
        else:
            print_cards(self.dealer.hand.cards, hidden=True)
            print("Value: ???")

        print("\nYour Hand:")
        print_cards(self.player.hand.cards)
        print(f"Value: {self.player.hand.value()}")
        print("\n")

    def player_turn(self):
        while True:
            if self.player.hand.value() >= 21:
                break

            choice = input("Hit (h) or Stand (s)? ").lower()
            if choice == "h":
                self.player.hit(self.deck)
                self.clear()
                self.show_hands()
            else:
                break

    def dealer_turn(self):
        self.clear()
        self.show_hands(reveal_dealer=True)
        time.sleep(1)

        while self.dealer.hand.value() < 17:
            self.dealer.hit(self.deck)
            self.clear()
            self.show_hands(reveal_dealer=True)
            time.sleep(1)

    def determine_winner(self):
        p = self.player.hand.value()
        d = self.dealer.hand.value()

        print("\n==========================")
        print("        RESULTS")
        print("==========================")

        if p > 21:
            print("You busted! Dealer wins.")
        elif d > 21:
            print("Dealer busts! You win! 🎉")
        elif p > d:
            print("You win! 🎉")
        elif d > p:
            print("Dealer wins.")
        else:
            print("It's a tie!")

    def play(self):
        self.clear()
        self.deal_initial_cards()
        self.show_hands()

        # Player turn
        self.player_turn()

        # Dealer turn
        self.dealer_turn()

        # Winner
        self.determine_winner()


# -------------------------------
# MAIN LOOP
# -------------------------------

if __name__ == "__main__":
    while True:
        game = BlackjackGame()
        game.play()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break
