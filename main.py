#!/usr/bin/env python3
"""project: Rock Paper Scissors
created:2021-09-23, @author:seraph★776, email:seraph776@gmail.com"""

# Import ranodm module
from random import choice, randint

def main():
    
    # Start main loop
    while True:
        ht = {1: 'rock', 2: 'paper', 3: 'scissors'}         
        while True: # Ask user to enter Rock, paper Scissors      
            user_choice = input('Enter (1)rock, (2)paper, (3)sissors:\n> ')
            # Get computer's choice 
            computer_choice = ht.get(randint(1, 3))
            if user_choice not in '123':
                print('Invalid input')
                continue
            else:
                break

        # Change user_choice dataype to integer
        user_choice = ht.get(int(user_choice))

        # Calculate winner
        if user_choice == computer_choice:
            print(f"{user_choice} vs {computer_choice}")
            print("It's a draw\n")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"{user_choice} vs {computer_choice}")
            print("Player wins!\n")
        else:
             print(f"{user_choice} vs {computer_choice}")
             print("Computer wins!\n")



if __name__ == '__main__':
    main()



