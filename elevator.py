"""
Calculate the expected the number of floors that 10 independent people would want to stop in a 10-floor building, assuming all 10 enter the elevator on the ground floor and no one else enters the elevator at any other floor. 
"""

import random
from matplotlib import pylab as plt

def elevator():
    n = 10000
    estimates = []
    floors = range(1, 11) # 10 floors
    count_floors = 0
    for i in range(n):
        choices = [random.choice(floors) for a in range(10)] # 10 independent selections of a floor
        choiceset = set(choices) # get rid of repeats
        count_floors += len(choiceset) # count distinct floor
        estimates.append(count_floors / (float(i+1)))

    plt.figure(1)
    plt.semilogx(estimates)
    plt.xlabel("log(number of samples)")
    plt.ylabel("estimated probability")
    plt.title("Estimating the Expected Number of Elevator Stops")
    plt.show()

if __name__ == "__main__":
    elevator()
