import sys
import time
from datetime import datetime
from random import randint
import sqlite3
import funcs
from classes import Player 


MAX = 6
conn = sqlite3.connect('hangman_data.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Player') # for debugging purposes

cur.execute('''CREATE TABLE IF NOT EXISTS Player
    (User TEXT UNIQUE, Points INTEGER, Entry DATETIME)''')


print('--------THE HANGMAN GAME--------')
name = input('USER NAME: ').upper()
entry = datetime.now()

funcs.start(name, entry, cur)

user = Player(name, cur, conn)

while True:
    rules = input("--------ENTER 'R' TO VIEW RULES ELSE PRESS ENTER\n").upper()
    if rules == 'R': funcs.see_rules()
    
    print("IF YOU WOULD LIKE A HINT AT ANYTIME, ENTER '1' (ONE).")
    print("IF YOU WOULD LIKE TO SKIP THIS ROUND, ENTER '2' (TWO).")
    print(f'--------ROUND {user.round}--------')
    
    word, definition = funcs.questions()
#     print(f'word = {word}') # for debugging purposes
    
    question = ' '.join([x if x == ' ' else '_' for x in word])
    print(question)
    
    result = False
    
    while not result and user.tries < MAX:
        letter = input('GUESS: ').upper()
        if letter == '1': 
            user.hint(word, question, definition)
            letter = input('GUESS: ').upper() # can't skip round directly after calling '1'
        elif letter == '2':
            result = None
            break
        
        question, result = user.guess(letter, word, question)
        print(f'NUMBER OF TRIES REMAINING: {MAX - user.tries}')
        print(f'LETTERS GUESSED: {user.guessed}')
        print(question)
    
    if result: 
        print('--------CONGRATULATIONS! YOU WON THE ROUND!--------')
    elif result == False:
        print('--------SORRY, THERE ARE NO MORE TRIES LEFT. YOU LOSE!--------')
        print(f'--------WORD = {word}--------')
    
    print('USER DETAILS...\n'
         f'USER NAME: {name}\n'
         f'POINTS THIS ROUND: {user.add_point}\n'
         f'OVERALL POINTS: {user.points}\n'
         f'NUMBER OF WRONG GUESSES: {user.tries}\n')
    
    quit = input('--------WOULD YOU LIKE TO QUIT? [Y/N]-------- \n').upper()
    if quit == 'Y': sys.exit() 
    
    user.reset()
    
conn.close()
