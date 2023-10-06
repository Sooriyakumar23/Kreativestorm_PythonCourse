'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

import random

game_words = ['javascript', 'python', 'html', 'java', 'css', 'cpp', 'c']
game_word_string = random.choice(game_words).lower()
game_word = list(game_word_string)

word = ['_'] * len(game_word)
max_guess = 6
total_guess = 0

used_letters = ''

isSuccess = False

while ((total_guess < max_guess) and (not(isSuccess))):
    print(f'You have {max_guess-total_guess} tries left.')
    print ('Used letters: ' + used_letters)
    print ('Word: ', ''.join(str(j) for j in word))
    guess = input('Guess a letter: ').lower()

    used_letters += guess + ' '

    isNotCorrectGuess = True
    for index, character in enumerate(game_word):
        if (character == guess):
            word[index] = guess
            isNotCorrectGuess = False
    
    if (game_word == word):
        isSuccess = True
    
    if (isNotCorrectGuess):
        total_guess += 1

    print ('\n')

if (isSuccess):
    print (f'You guessed the word {game_word_string} !')
else:
    print ('Sorry, Game is over')