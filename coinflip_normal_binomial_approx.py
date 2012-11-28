"""
In this problem, we want to test if the probability of getting at least 5064 heads out of 10000 flips of a fair coin is approximately 0.10 by the normal approximation to a binomial random variable
"""

import random
from matplotlib import pylab as plt

def flip():
    n = 10000
    num_heads = 0
    for i in range(n):
        outcome = random.randint(0, 1) # 0 for Head, 1 for Tail
        if outcome == 1:
            num_heads += 1
    return num_heads

def simulate():
    simulation = 1000 # 1000 simulation
    num_pass_threshold = 0
    estimates = []
    for i in range(simulation):
        result = flip()
        if result > 5064:
            num_pass_threshold += 1
        estimates.append(num_pass_threshold / (float(i+1)))

    plt.figure(1)
    plt.semilogx(estimates)
    plt.xlabel("log(number of samples)")
    plt.ylabel("estimated probability")
    plt.title("Estimating the Probability of the Number of Heads from 10000 Flips of a Fair Coin")
    plt.show()

if __name__ == "__main__":
    simulate()
