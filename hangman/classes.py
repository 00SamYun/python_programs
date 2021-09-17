import sqlite3 
import random


class Player():
    '''
    tracks player progress
    '''
    def __init__(self, name, cursor, conn): 
        
        self.name = name
        self.guessed = [] # list of guessed letters
        self.round = 1 # each new word is a new round
        
        self.cur = cursor
        self.conn = conn
        self.cur.execute('SELECT Points FROM Player WHERE User=?', (self.name, ))
        self.points = self.cur.fetchone()[0] 
        self.add_point = 0
        self.tries = 0
    
    
    def update(self):
        '''
        updates any change in points in the program & the database
        '''
        
        self.points += self.add_point
        self.cur.execute('UPDATE Player SET Points=? WHERE User=?', 
            (self.points, self.name))
        self.conn.commit()
        
        
    def point(self):
        '''
        calculates points gained each round based on number of wrong guesses
        '''
        
        if self.tries <= 1:
            self.add_point = 500
        elif self.tries <= 3:
            self.add_point = 300
        else:
            self.add_point = 100
            
    
    def hint(self, word, ques, meaning):
        '''
        prints a hint based on the number of points the player has
        : param word: target word
        : param ques: current progress; combination of _ and letters
        '''
        
        VOWELS = 'aeiou'
        ques = ques.split()
        
        if self.points < 100:
            print('SORRY, YOU NEED AT LEAST 100 POINTS FOR A HINT.')
            return
        elif self.points < 200:
            choice = 'A'
        else:
            choice = input('--------PICK ONE HINT--------\n'
                         'GENERIC -------- 100 POINTS (A)\n'
                         '1 LETTER ------- 200 POINTS (B)\n'
                          'DEFINITION ---- 400 POINTS (C)\n').upper()
        
        letters = [word[i] for i,x in enumerate(ques) if x == '_']
        vowel_check = [l for l in letter if l in VOWELS]
        
        if choice == 'A':
            self.add_point = -100
            self.update()
            if len(vowel_check) == 1:
                print(f'THERE IS 1 VOWEL LEFT.')
            else:
                print(f'THERE ARE {vowel_check} VOWELS LEFT.')
        
        elif choice == 'B':
            self.add_point = -200
            self.update()
            letter = random.choice(letters)
            print(f'ONE OF THE LETTERS IS {letter}')
            
        elif choice == 'C':
            self.add_point = -400
            self.update()
            print(f'DEFINITION: {meaning}')
            
            
    def guess(self, x, word, ques):
        '''
        returns True if the word is guessed and False otherwise
        : param x: the letter that is guessed 
        : param word: target word
        : param ques: current progress; combination of _ and letters
        '''
        
        if not x.isalpha() or len(x)!=1: 
            print('PLEASE ONLY ENTER AN ALPHABET.')
            return ques, False
        
        if x in word:
            ques = ques.split()
            pos = [i for i,l in enumerate(word) if l == x]
            ques = [x if i in pos else l for i,l in enumerate(ques)]
            ques = ' '.join(ques)
        elif x not in self.guessed:
            self.guessed.append(x)
            self.tries += 1
        
        if '_' not in ques: return ques, True
        
        return ques, False
    
    
    def reset(self):
        self.tries = 0
        self.guessed = []
        self.round += 1
