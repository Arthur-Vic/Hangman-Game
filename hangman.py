
'''
__\n
| |\n
| |____   ______   _  ___   ______   _  ___  ___   ______   _  ___ \n
|  __  | | __   | | |/_  | |  __  | | |/_  |/_  | | __   | | |/_  |\n
| |  | | | |_|  | |  / | | |  |_| | |  / |  / | | | |_|  | |  / | |\n
|_|  |_| |___/|_| |_/  |_| |____  | |_/  |_/  |_| |___/|_| |_/  |_|\n
                            _   | |\n
                           | |__| |\n
                           |______|\n
                           '''

'''
 ____\n
|    |\n
|    O\n
|   /|\\\n
|   / \\\n
|\n
| _ _ _ _ _ _ _
'''

import random

def title():
    print('__\n| |\n| |____   ______   _  ___   ______   _  ___  ___   ______   _  ___ \n|  __  | | __   | | |/_  | |  __  | | |/_  |/_  | | __   | | |/_  |\n| |  | | | |_|  | |  / | | |  |_| | |  / |  / | | | |_|  | |  / | |\n|_|  |_| |___/|_| |_/  |_| |____  | |_/  |_/  |_| |___/|_| |_/  |_|\n                            _   | |\n                           | |__| |\n                           |______|\n')
    
title()

start = ''
while start != 'start':
    start = input('Type START to begin playing: ').lower().strip()
    if start != 'start':
        print('Invalid Command')

words_list = ['ROPO']
word = random.choice(words_list)
number_of_dashes = len(word)
blank_array = ['_'] * number_of_dashes

head = 'O'
arm1 = '/'
arm2 = '\\'
torso = '|'
leg1 = '/'
leg2 = '\\'

hangman = [head, arm1, torso, arm2, leg1, leg2]
blank_hangman = [' ',' ',' ',' ',' ',' ']

print(f' ____\n|    |\n|    {blank_hangman[0]}\n|   {blank_hangman[1]}{blank_hangman[2]}{blank_hangman[3]}\n|   {blank_hangman[4]} {blank_hangman[5]}\n|\n|', end = '')

for dash in blank_array:
    print (' ' + dash, end = '')

print ('')

player_lives = 6
index = (player_lives * -1)

def loose_life():
    global player_lives
    index = (player_lives * -1)
    blank_hangman[index] = hangman[index]
    player_lives -= 1

#GAME START -----------------------------------------------------------

while ' ' in blank_hangman:
    if '_' not in blank_array:
        print ('YOU WIN!!')
        break

    letter = input('Guess a letter: ').upper().strip()

    if letter in word:
        while letter in word:
            letter_index = word.find(letter)
            blank_array[letter_index] = letter
            word_array = list(word)
            word_array[letter_index] = ' '
            word = ''.join(word_array)
    else:
        loose_life()

    print(f' ____\n|    |\n|    {blank_hangman[0]}\n|   {blank_hangman[1]}{blank_hangman[2]}{blank_hangman[3]}\n|   {blank_hangman[4]} {blank_hangman[5]}\n|\n|', end = '')

    for dash in blank_array:
        print (' ' + dash, end = '')

    print ('')
    print (f'Lives: {player_lives}')
    print ('')
    print(word)
    #print(blank_hangman)   #Debugging


print('GAME OVER')