"""
********************************************** Description ************************************************
                                                                                                          *
Create a classic game named hangman.                                                                      *
To start with, you should pick a random word from "WORDS" list, and the user must guess the word.         *
Whenever a user enters some char,                                                                         *
if it's in our word, show it in the appropriate place (char could be several places at once).             *
Whenever that character is not found in our word, the number of trials (LIFE_NUMBER) is reduced by one.   *
The game ends when the user guesses the word or LIFE_NUMBER reaches zero                                  *
Ask the user if they want to play again after the game ends                                               *
                                                                                                          *
                                                                                                          *
input:                                                                                                    *
    assume computer chose word "disappear"                                                                *
    m                                                                                                     *
output:                                                                                                   *
    _________                                                                                             *
                                                                                                          *
                                                                                                          *
input:                                                                                                    *
    assume computer chose word "disappear"                                                                *
    a                                                                                                     *
output:                                                                                                   *
    ___a___a_                                                                                             *
                                                                                                          *
                                                                                                          *
P.S                                                                                                       *
    we don't test this exercise result, so you can use all prints and user inputs as you want             *
    random.randint(start, stop) will return a number between start and stop                               *
    think about join() and split() functions                                                              *
    use decomposition and write several functions with comments                                           *
                                                                                                          *
                                                                                                          *
********************************************** good luck **************************************************
"""

import random


LIFE_NUMBER = 3

""" I use list to store all possible words """
WORDS = ["aunt", "strange", "broad", "stale", "craven", "disappear", "wistful", "rustic", "bushes", "splendid",
         "aftermath", "shallow", "demonic", "vessel", "tenuous", "hungry", "possible", "wasteful", "finicky", "bounce"
         "scissors", "spectacular", "adamant", "knotty", "chief", "locket", "telling", "harbor", "stick", "dislike"]


# Define all the functions what you need

def start_game():
    # write your code here
    pass
