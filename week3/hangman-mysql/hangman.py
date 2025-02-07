#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import random
import pymysql
import sys

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

try:
    conn = pymysql.connect(host="localhost", user="root", password="1234", db="mydb", charset='utf8')
    curs = conn.cursor()
    curs.execute("select * from word")
except:
    print("sql load error")
    sys.exit()

words = [ word[1] for word in curs.fetchall() ]

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord, highestScore, score):
    print(HANGMANPICS[len(missedLetters)])
    print()
    if(highestScore):
        print("Highest Score:",highestScore,end=' ')
    else:
        print("Highest Score: None",end=' ')
    print("Score:",score,end=' ')
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = ''
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks += secretWord[i]
        else:
            blanks += '_'

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# Check if the player has won
def checkCorrectAnswer(correctLetters, secretWord):
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    return foundAllLetters

# Check if player has guessed too many times and lost
def checkWrongAnswer(missedLetters, secretWord):
    # Check if player has guessed too many times and lost
    if len(missedLetters) == len(HANGMANPICS) - 1:
        return True
    return False

# Load Highest Score
def loadScore():
    sql = "select * from score"
    curs.execute(sql)
    scores = [ int(score[1]) for score in curs.fetchall() ]
    print(scores)
    if(len(scores)):
        return max(scores)
    return None
    
# Update Highest Score
def updateScore(highestScore, score):
    sql = "insert into score (score) values (%s)"
    curs.execute(sql, score)
    conn.commit()

def main():
    """Main application entry point."""
    print('H A N G M A N by ...')
    missedLetters = ''
    correctLetters = ''
    gameSucceeded = False
    gameFailed = False
    secretWord = getRandomWord(words)
    highestScore = loadScore()
    score = 0
    
    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord,highestScore, score)

        if gameSucceeded or gameFailed:
            updateScore(highestScore, score)
            if gameSucceeded:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
            else:
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

            # Ask the player if they want to play again (but only if the game is done).
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameSucceeded = False
                gameFailed = False
                secretWord = getRandomWord(words)
                highestScore = loadScore()
                score = 0
                continue 
            else:
                conn.close() 
                break

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            gameSucceeded = checkCorrectAnswer(correctLetters, secretWord)
        else:
            missedLetters = missedLetters + guess
            gameFailed = checkWrongAnswer(missedLetters, secretWord)
        score = len(correctLetters) -  len(missedLetters)


if __name__ == "__main__":
    main()
