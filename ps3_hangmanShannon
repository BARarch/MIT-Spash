# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string 

WORDLIST_FILENAME = "/Users/shannnonliburd/Desktop/Desktop/Python/psets/6.001 pset 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    lettersGuessed=''.join(lettersGuessed)

    count=0
    for char in lettersGuessed: #for each character in lettersGuessed
        if char in secretWord: #will check if the character in lettersGuessed is in secretWord
          count += 1 #increment count by 1 if share character

    if count==len(secretWord):
        return True
    else: 
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    n=len(secretWord)
    secretWord=list(enumerate(secretWord))
    dct=dict(secretWord)
    lettersGuessed=''.join(lettersGuessed)

    display=[' _ ']*n


    for char in lettersGuessed: #for each character in lettersGuessed
        if char in dct.values(): #will check if letter in dictionary values 
         while True:
          for i in range(0,n): # if letter in values, display it
              if char==dct.get(i):
                  key=i
                  display[key]=dct[key]
          break
    strDisplay=''.join(display)         
    return strDisplay # display as string what letters in dictionary match secret word  
     




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersGuessed=''.join(lettersGuessed) # convert to a string 
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabetList=list(alphabet) 
    CloneAlphabetList=alphabetList[:]

    for char in lettersGuessed:
        if char in alphabetList: #checks to see if letter in alphabetList
          for i in range(0,len(CloneAlphabetList)):
            if alphabetList[i]==char: # if letter in alphabetList delete it
                del(alphabetList[i]) 
                break
    remainingLetters=''.join(alphabetList) # converts remaining letters to a string 
    return remainingLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    lettersGuessed=[] #The letters that have been guessed so far.
    availableLetters=[] # The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed.
    n=8 # total number of guesses available initially
    mistakesMade=0 # number of incorrect guesses
    guessesLeft=n-mistakesMade # number of guesses left until the game ends
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ", len(secretWord), " letters long.")
    
   
    
    while guessesLeft>0:
  
      #if guessesLeft==8: # Condition where just starting to play game
        if guessesLeft==n   : # Condition where just starting to play game [Anthony] This part is no longer nessesary see below.
            # [Anthony] place this chunk before the loop, it will not work if the player makes a good guess on the first shot
         print("You have", guessesLeft, "guesses left.")
         print ("Available letters: ", string.ascii_lowercase)
         guess=input("Please guess a letter: ").lower()
         lettersGuessed.append(guess) # add letter to the end of list
         availableLetters=lettersGuessed[:]
     
     
         for char in lettersGuessed: #for each character in lettersGuessed
             if char in secretWord: #will check if the character in lettersGuessed is in secretWordif lettersGuessed[i]==secretWord[i]: # case                                          where letter guessed mataches letter in secret word
               print("Good guess: ", getGuessedWord(secretWord,lettersGuessed))
               lettersGuessed.append(guess) # add letter to the end of list
               availableLetters=lettersGuessed.pop() # remove letter from end of list
               print("You have", guessesLeft, "guesses left.")
               print ("Available letters: ", getAvailableLetters(availableLetters))
               guess=input("Please guess a letter: ").lower()
               
           
             else:  
                mistakesMade+=1
                guessesLeft=n-mistakesMade
                print("You have", guessesLeft, "guesses left.")
                print("Available letters: ", getAvailableLetters(lettersGuessed))
                print('Oops! That letter is not in my word: ',getGuessedWord(secretWord,lettersGuessed) )
                guess=input("Please guess a letter: ").lower()
                lettersGuessed.append(guess)
           
          
      if guessesLeft<8: # Condition where just starting to play game
         print("You have", guessesLeft, "guesses left.")
         print ("Available letters: ", getAvailableLetters(lettersGuessed))
         guess=input("Please guess a letter: ").lower()
         lettersGuessed.append(guess)
         
       
         for char in lettersGuessed: #for each character in lettersGuessed
             if char in secretWord: #will check if the character in lettersGuessed is in secretWordif lettersGuessed[i]==secretWord[i]: # case where letter guessed mataches letter in secret word
               print("Good guess: ", getGuessedWord(secretWord,lettersGuessed))
               lettersGuessed.append(guess)
               availableLetters=lettersGuessed.pop()
               print("You have", guessesLeft, "guesses left.")
               print ("Available letters: ", getAvailableLetters(lettersGuessed))
               guess=input("Please guess a letter: ").lower()
             
             elif guess not in lettersGuessed:
                 print("You have", guessesLeft, "guesses left.")
                 print ("Available letters: ", getAvailableLetters(availableLetters))
                 guess=input("Please guess a letter: ").lower()
                 print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

           
             else:  
                mistakesMade+=1
                guessesLeft=n-mistakesMade
                print("You have", guessesLeft, "guesses left.")
                print("Available letters: ", getAvailableLetters(lettersGuessed))
                print('Oops! That letter is not in my word: ',getGuessedWord(secretWord,lettersGuessed) )
                guess=input("Please guess a letter: ").lower()
                lettersGuessed.append(guess)
           
          
         
         else:
           GameOver=isWordGuessed(secretWord, lettersGuessed) 
           if GameOver==True:
                  print("Congratulations, you won!")
           else:
                  print("Sorry, you ran out of guesses. The word was",secretWord, ". ")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord=input("Enter your secret word: ").lower()

# secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
