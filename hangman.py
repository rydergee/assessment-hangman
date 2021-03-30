import random
import os

# Terminal Colours
CBLUE = "\033[94m"
CGREEN = "\033[92m"
CRED = "\033[91m"
CEND = "\033[0m"


TITLE = """
--------------------------------------
  _  _                                
 | || |__ _ _ _  __ _ _ __  __ _ _ _  
 | __ / _` | ' \/ _` | '  \/ _` | ' \ 
 |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
                |___/                 
--------------------------------------                     
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Keep asking user question until answer is valid
def askUser(question, valid_inputs):
    response = input(question)
    while True:
        for correct in valid_inputs:
            if response == correct:
                return response
            else:
                continue    
    
# Load list of words from word_list.txt file
def get_dictionary():
    with open("word_list.txt", "r") as words:
        dictionary = []
        lines = words.readlines()
        for line in lines:
            dictionary.append(line.replace("\n", ""))
        return dictionary

# Get a word from word list based on its length
def get_word(word_length):
    dictionary = get_dictionary()
    word = random.choice(dictionary)
    while len(word) != word_length:
        word = random.choice(dictionary)
    return word

# Get specified hangman graphic from hangman_graphics.txt
def get_graphic(value):
    graphic = []
    lines_to_read = [lines for lines in range(8*value-8, 8*value)]
    with open("hangman_graphics.txt") as graphics:
        for position, line in enumerate(graphics):
            if position in lines_to_read:
                graphic.append(line.replace("\n",""))
        return graphic

# Check the users guess if it has any occurences in the word 
def guess(user_guess, solved, word):
    user_guess = user_guess.upper()
    word = word.upper()
    for letter in word:
        if user_guess == letter:
            # Gather all occurences of letter
            occurences = [i for i in range(len(word)) if word.find(user_guess, i) == i]
            # Add each occurence to what the user has solved so far
            for occurence in occurences:
                solved[occurence] = user_guess
            print("You guessed '{}' and it was {}correct{}!".format(user_guess, CGREEN, CEND))
            return [solved, True]
    print("You guessed '{}' and it was {}incorrect{}!".format(user_guess, CRED, CEND))
    return [solved, False]
