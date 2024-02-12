#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:56:47 2021

@author: kali
"""
import random
import time
from hangman_visual import lives_visual_dict
from words import words

# Initial steps to invite in the game:
print("\nWelcome to Hangman game")
myName = input("Enter your name: ")
print("Hello " + myName + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]
def displayBoard(lives_visual_dict, missedLetters, correctLetters, secretWord):
    print(lives_visual_dict[len(missedLetters)])
    print()
    
    print('Missed letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end='')
    print()
    
def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if  len(guess) != 1:
            print('My dear friend, Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Hey ' + myName + '!, You have already Guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('My dear friend, Please enter a LETTER.')
        else:
            return guess
        
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns Flase.
    play_game = input('Do You want to play again?(yes or no) \n')
    while play_game not in ["n", "y", "N", "Y"]:
        play_game = input('Do You want to play again? y = yes, n = n0 \n')
    if play_game == 'n':
        print("Thanks For Playing! we expect you back again!")
    return play_game.lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(lives_visual_dict, missedLetters, correctLetters, secretWord)
    
    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Congrats! You have guessed the word correctly!")
            time.sleep(1)
            print('Yes! The secretword is "'+ secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(lives_visual_dict) - 1:
            displayBoard(lives_visual_dict, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) +' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            time.sleep(2)
            print('Oh No!, My Dear friend, You lost the game.')
            time.sleep(2)
            print('No problem My Dear friend please try again next time.')
            time.sleep(2)
            gameIsDone =True
      # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
          if playAgain():
              missedLetters = ''
              correctLetters = ''
              gameIsDone = False
              secretWord = getRandomWord(words)
          else:
               break
           
        
            
