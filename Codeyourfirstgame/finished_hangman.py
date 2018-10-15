import random

###THIS IS THE FILLED OUT HANGMAN SCRIPT from GIAG MedTech session 08-10-2018###

#dictionary file with all the words for the game
word_file = "popular.txt"

#write a function that picks a word for the player to guess
def pick_word():
  
  #start with opening the word file
  with open(word_file) as f:
    #save all the words into a variable
    words=list(f)
  
  #pick a random word from the list
  while True:
    word = random.choice(words).strip().lower()
    return word

#function for asking the player for the guesses
def ask():
  guess = input("Guess? ")
  return guess

#function for checking if the guess is in the target word
def update(target, answer, guess):
  if guess in target:
    new_answer=""
    for i, l in enumerate(target):
      if l == guess:
        new_answer += guess
      else:
        new_answer += answer[i]
    return new_answer, 0
  else:
    return answer, 1

#draw the pictures for the hangman guesses
#we have made some for you in hangman_pic.txt
HANGMANPICS = [''' ''','''

      
      
      
      
      
=========''','''

      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
     /|
=========''', '''
  +---+
  |   |
      |
      |
      |
     /|
=========''','''
  +---+
  |   |
  O   |
      |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
     /|
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
     /|
=========''']

#Connect the functions into a game

#pick a random word and save it into a variable
target = pick_word()

#prepare how the secret answer is displayed
answer = "_ "*len(target)

#set a varaible to count the mistakes
mistakes = 0
#keep track of all the guesses
sofar = []

while True:
  #what is displayed to the player
  print(answer)
  print(sofar)
  print("Mistakes", mistakes)
  print(HANGMANPICS[mistakes])
  print("You are doing great!")

  #ask for the guess
  guess = ask()

  #update the guesses so far
  sofar.append(guess)

  #check if the guess matches the answer
  answer, c = update(target, answer, guess)

  #update the mistakes counter
  mistakes = mistakes + c

  #end of game outcomes
  #if more mistakes than hangman pics, the game is over
  if mistakes >= len(HANGMANPICS)-1:
    print("GAME OVER!")
    print("The answer was:", target)
    break

  # if answer is the same as the target word,the player has won
  if answer == target:
    print("Well done! You are amazing!")
    break