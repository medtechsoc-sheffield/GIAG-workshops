import random

###THIS IS AN EMPTY SCRIPT WITH SUGGESTIONS FOR OPTIONAL FEATURES###

#dictionary file with all the words for the game
word_file = "popular.txt"

#write a function that picks a word for the player to guess
def pick_word():
  
  #start with opening the word file

    #save all the words into a list variable

  
  #pick a random word from the list

    #optional: make it harder by only picking words that are longer than 4 letters
    #optional: make sure that the random "word" is made of letters
    return word

#optional: modify how the answer gets printed to the player

#function for asking the player for the guesses
def ask():
  
  #optional: check the quality of the guess
  #optional: check the guess is only one letter
  return guess

#function for checking if the guess is in the target word
def update(target, answer, guess):
  if guess in target:
    new_answer = "" 
    



    return new_answer
  else:
    return new_answer

#draw the pictures for the hangman guesses
#we have made some for you in hangman_pic.txt

###Connect the functions into a game

#optional: do you want to start the game
#optional: ask the player to paly again at the end

#pick a random word and save it into a variable
target = 
#prepare how the secret answer is displayed
answer = 
#set a varaible to count the mistakes
mistakes = 
#keep track of all the guesses
sofar = []

while True:
  #what is displayed to the player

  #ask for the guess

  #update the guesses so far

  #check if the guess matches the answer

  #update the mistakes counter

  #end of game outcomes
  #if more mistakes than hangman pics, the game is over

  # if answer is the same as the target word,the player has won
