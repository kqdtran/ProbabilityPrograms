"""
Calculate the probability of a straight hand in a game of poker.
See https://en.wikipedia.org/wiki/List_of_poker_hands#Straight for more details
"""

import random
from matplotlib import pylab as plt

def cards():
    n = 10000
    estimates = []
    deck = range(13)*4 # Ranks represented as numbers 0-12. 4 of each rank in deck
    straights = [range(5), range(1, 6), range(2, 7), range(3, 8), range(4, 9), range(5, 10), range(6, 11), range(7, 12), range(8, 13), range(4) + [12]]
    # 9 different ways to have a straight
    # E.g. range (5) is 2-3-4-5-6
    # range(4) + [12] is A-2-3-4-5, but listed as 2-3-4-5-A

    count_straights = 0 # record the number of observed straights
    for i in range(n):
        hand = random.sample(deck, 5) # get a random sample of 5 elements from the deck
        hand = sorted(hand) # sort the cards in ascending order
        if hand in straights: # check to see if this hand is a straight
            count_straights += 1
        estimates.append(count_straights / (float(i+1)))
        # the formula is estimate = (num observations / num trials)

    plt.figure(1)
    plt.semilogx(estimates)
    plt.xlabel("log(number of samples)")
    plt.ylabel("estimated probability")
    plt.title("Estimating the Probability of a Poker Straight")
    plt.show()
    
if __name__ == "__main__":
    cards()
