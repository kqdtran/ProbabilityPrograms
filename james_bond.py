from __future__ import division 
import random

def bond_escape():
    total_time = 0
    choice = random.randint(1, 3)
    
    while choice != 3:
        if choice == 1: # choose air_conditioning duct
            total_time += 2
        elif choice == 2: # choose sewer pipe
            total_time += 5
        choice = random.randint(1, 3)
        
    return total_time

def main():
    s = raw_input("How many trials should Bond go through? Please enter a positive integer: ")
    try:
        num_trial = int(s)
        if num_trial > 0:        
            total_time = 0
            for i in range(num_trial):
                total_time += bond_escape()
            print "Expected time for JBond to escape with", num_trial, "trials is:", total_time / num_trial
        else:
            print "You didn't enter a positive integer :("
            main()
    except ValueError:
        print "You didn't enter an integer :("
        main()
    
if __name__ == "__main__":
    main()
