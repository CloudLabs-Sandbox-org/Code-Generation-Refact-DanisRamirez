# Intentionally fixed Python program

# importing modules
import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
def draw_cards():
    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])

if __name__ == "__main__":
    draw_cards()
