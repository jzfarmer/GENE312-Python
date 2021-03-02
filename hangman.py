# Welcome to Nat and Jess's GENE312 Final Project 
# Hope you like genetics and python because you're in for a real treat 

import random
import pandas as pd
import numpy as np


filename = 'hintsandwords.csv'
df = pd.read_csv(filename, header=0)   # read the file w/header row #0
# print(f"{filename} : file read!")

A = df.values
# print(A)

COLS = {              # also: FEATURES
    'hint':0,
    'word':1,
}
# test this
# print("Test COLS:  COLS['hint'] is", COLS['hint'])

def get_word():
    E = random.choice(A)
    return E[1].upper(), E[0]

def play():
    word, question = get_word()
    #print("the hidden word is", word)
    word_completion = "_" *len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  # number of body parts on hangman before he dies
    print("Let's play Hangman! I hope you know your genetics because my life's on the line!")
    print(question)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0: 
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter, silly goose", guess)
            elif guess not in word:
                print(guess, "is not in the word")  
                tries -= 1  
                guessed_letters.append(guess)
            else:
                print("Good job, look at you chap", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess, we're only guessing letters here")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win and didn't let me die!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". How could you let me die?!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      💀
                   |    🦾🥼🤳
                   |      👖
                   |     🦵🦵
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      😭
                   |    🦾🥼🤳
                   |      👖
                   |       🦵
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      😕 
                   |    🦾🥼🤳
                   |     
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      😑
                   |    🦾🥼
                   |      
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      😐
                   |      🥼
                   |     
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      🥺
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    play()
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play()

if __name__ == "__main__":
    main()
