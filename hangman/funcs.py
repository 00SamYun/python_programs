import sqlite3
import time
import requests


def start(user, entry, cursor):
    '''
    checks the database to see if the user is a new or returning player
    prints the introduction
    '''
    
    cursor.execute('SELECT User, Points, Entry FROM Player')
    returning = [row for row in cursor if user == row[0]]
    
    if returning:
        user, points, entry = returning[0]
        print(f'WELCOME BACK, {user}')
        time.sleep(0.5)
        print(f'TOTAL POINTS GAINED SO FAR --- {points}')
        time.sleep(0.5)
        print(f'LAST ENTRY WAS ON ------------ {entry}')

    else:
        print(f'WELCOME TO YOUR FIRST HANGMAN GAME, {user}')
        time.sleep(0.5)
        print('YOU WILL START WITH --- 0 --- POINTS')
        time.sleep(0.5)
        cursor.execute('''INSERT OR IGNORE INTO Player (User, Points, Entry)
            VALUES (?, 0, ?)''', (user, entry))
    

def see_rules():
    '''
    prints out the rules of the game
    '''
    print('''--------RULES OF THE HANGMAN GAME--------\n
        1. The player begins with 6 lives\n
        2. In each try, the player is required to guess a letter\n
        3. If a correct letter is guessed, it replaces the _ in the word\n
        4. If an incorrect letter is guessed, the player loses a life\n
        5. The incorrect letter will be displayed in the 'guessed' section\n''')
    
    cont = input("----'M' FOR MORE INFO | 'B' FOR BACK----\n").upper()
    
    if cont == 'M':
        print('''--------HOW TO WIN--------\n
        1. A player wins if the entire word is guessed before he loses all lives\n
        2. A player loses if he fails to guess the word after 6 incorrect tries\n
        3. The number of points gained depends on the number of incorrect tries\n
        4. Points are important as they allow you to get hints''')
        
        print('''--------HINTS--------\n
        1. There are 3 types of hints that can be used\n
        2. 100 points will get you the number of vowels\n
        3. 200 points will get you a letter\n
        4. 400 points will get you the definition of the word''')


def questions():
    '''
    returns a randomly selected word with its definition from an API 
    '''
    
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "<YOUR_API_KEY"
        }
    
    definition = ''
    
    while definition == '':
        word = requests.get(url, headers=headers, params={"random":"true"}).json()['word'].upper()
        
        definitions = requests.get(f'{url}{word}/definitions', headers=headers).json()['definitions']
        if definitions == []:
            definition = ''
        else:
            definition = definitions[0]['definition'].upper()
    
    return word, definition
