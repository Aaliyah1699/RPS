'''Rock Paper Scissors Game'''
import random
import os
import re

#1st function to check if the user wants to play
def play_status():
    valid_resopnse = ['yes', 'no']
    #while the response is True
    while True:
        #Try a response to see if they want to play again
        try:
            response = input('Do you want to play again?  (yes or no): ')
            #if they say something other than yes/ no raise value error with their options
            if response.lower() not in valid_resopnse:
                raise ValueError('Yes or No only')
            #if their answer is yes return True
            if response.lower() == 'yes':
                return True
            #else use os to clear and exit game
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()
        #Except value error as err and print err
        except ValueError as err:
            print(err)
#2nd func for playing the game var = True

#While  var: use os and print rps + ask user what they'll use

#if not an option using re then ask them to put correct option + continue

#print users choice using f str

#2 var 1st is playing options / 2nd random choice

#print computer choice

#Execute code if file is ran directly not imported
if __name__ == '__main__':
    play_game()