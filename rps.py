'''Rock Paper Scissors Game'''
import random
import os
import re

# 1st function to check if the user wants to play


def play_status():
    valid_response = ['yes', 'no']
    # while the response is True
    while True:
        # Try a response to see if they want to play again
        try:
            response = input('Do you want to play again?  (yes or no): ')
            # if they say something other than yes/ no raise value error with their options
            if response.lower() not in valid_response:
                raise ValueError('Yes or No only')
            # if their answer is yes return True
            if response.lower() == 'yes':
                return True
            # else use os to clear and exit game
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()
        # Except value error as err and print err
        except ValueError as err:
            print(err)
# 2nd func for playing the game var = True


def play_game():
    play = True
    # While  var: use os and print rps + ask user what they'll use
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors -> SHOOT!')
        user_pick = input('Chose your weapon ''[R]ock, [P]aper, [S]cissors: ')
        # if not an option using re then ask them to put correct option + continue
        if not re.match("[SsRrPp]", user_pick):
            print('Please chose a letter:')
            print('[R]ock, [P]aper, or [S]cissors ')
            continue
        # print users choice using f str
        print(f'You chose: {user_pick}')
        # 2 var 1st is playing options / 2nd random choice
        choices = ['R', 'P', 'S']
        ran_choice = random.choice(choices)
        # print computer choice
        print(f'I chose: {ran_choice}')
        # if both picks are the same print tie
        if ran_choice == user_pick.upper():
            print('TIE!')
            play = play_status()  # ask if they still want to play referring to first func
        # elif ran wins with rock
        elif ran_choice == 'R' and user_pick.upper() == 'S':
            print('Rock beats Scissors, I win!')
            play = play_status()
        # ran wins with scissors
        elif ran_choice == 'S' and user_pick.upper() == 'P':
            print('Scissors beat Paper, I win!')
            play = play_status()
        elif ran_choice == 'P' and user_pick.upper() == 'R':
            print('Paper beats Rock, I win!')
            play = play_status()
        # Else They win
        else:
            print('You Win!\n')
            play = play_status()


# Execute code if file is ran directly not imported
if __name__ == '__main__':
    play_game()
