# coding: utf-8
# Name: Jessica Farmer
# hw0pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        inputs: none        (prompted text doesn't count as an argument)
        outputs: none       (printing doesn't count as a result)
    """
    print('Wanna play a game?')
    print()
    user = input("Choose your weapon--rock, paper, or scissors:")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock':
        if comp == 'scissors':
            print('Ha! I really chose paper--I WIN!')
        elif comp == 'paper':
            print('Sorry, you lose kid.')
        else:
            print('It is a draw!')   
    elif user == 'scissors': 
        if comp == 'paper':
            print('I see you are feeling stabby. Put down the scissors and you win.')
        elif comp == 'rock':
            print('Get squished like a bug!')
        else:
            print('Aw man, a tie.')
    else:
        if comp == 'scissors':
            print('Easy win. Get owned.')
        elif comp == 'rock':
            print('Do you cheat at every game?')
        else:
            print('Tied up like a knot.')



    print("Let's play again!")
