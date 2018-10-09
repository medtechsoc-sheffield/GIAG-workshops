import random

###THIS IS THE BONES PF THE HANGMAN SCRIPT###

#dictionary file with all the words for the game
word_file = "popular.txt"

#write a function that picks a word for the player to guess
def pick_word():
  
  #start with opening the word file
  
    #save all the words into a variable
  
  
  #pick a random word from the list

    return

#function for asking the player for the guesses
def ask():

  return

#function for checking if the guess is in the target word
def update(target, answer, guess):
  #if guess is in the target word
  if :
    new_answer=""
    #update how the new answer is printed according to the new guess
    return
  #if guess is not in the target word
  else:
    return

#draw the pictures for the hangman guesses
#we have made some for you in hangman_pic.txt

#Connect the functions into a game

#pick a random word and save it into a variable
target = 

#prepare how the secret answer is displayed
answer = 

#set a varaible to count the mistakes
mistakes = 0
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
  if mistakes >= len(HANGMANPICS)-1:
    #print stuff
    break

  # if answer is the same as the target word,the player has won
  if answer == target:
    #print stuff
    break