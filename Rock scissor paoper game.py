
import random

def play():
    user_score = 0
    computer_score = 0

    while True:
        print("############################################################")
        user = input('''What's your choice from the following ... ? 
                     'r' for rock, 
                     'p' for paper, 
                     's' for scissors, 
                     'q' to quit\n _________________________:''').lower()
        print("############################################################")
        print(f"You entered: {user}")
        if user == 'q':
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            return

        if user not in ['r', 'p', 's']:
            print('''
                  oops.....!!! Invalid input. 
                  Please enter 'r', 'p', or 's'.
                  ''')
        else:
            computer = random.choice(['r', 'p', 's'])
            print(f"Computer chose: {computer}")

            print(f"\nYou chose {user}, computer chose {computer}.\n")

            if user == computer:
                print(f"Both players selected {user}. It's a tie! ....well played !!")
            elif is_win(user, computer):
                print('''exellent... !
                      You won this round ! 
                      congratulation ..!!''')
                user_score += 1
            else:
                print(''' oops ! 
                      You lost this round! 
                      you have worst played ''')
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}\n")

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()
