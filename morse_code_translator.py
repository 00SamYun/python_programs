# Only alphanumeric characters are translated
# In ENCODE mode, other characters are omitted

MORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }


def decode(code):
    '''
    code = a string of encoded text
    '''
    
    code_to_text = {v:k for k,v in MORSE.items()}
    
    code = code.split()
    text = [code_to_text[c] for c in code]
    
    return ''.join(text)

def encode(text):
    '''
    text = a string of plain text
    '''
    
    text_to_code = MORSE
    
    text = [t for t in text.lower() if t in text_to_code]
    text = [text_to_code[t] for t in text]
    
    return ' '.join(text)

def main():
    print('Please input the message you would like to encode/decode:')
    print('Note: To decode, please ensure the morse code'
    'for characters are separated by a space and words are separated by a space-slash-space " / ".')
    while True:
        msg = str(input('Message: '))
        if any([m.isalnum() for m in msg]):
            print('Encoded: ', encode(msg))
        else:
            print('Decoded: ', decode(msg))
      
    
if __name__ == '__main__':
    main()          
