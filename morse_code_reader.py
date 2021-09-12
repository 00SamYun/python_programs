from pynput.keyboard import Listener, Key
from time import time

DUR_TO_CODE = {1: '.', 3: '-'}
DUR_TO_SEP = {1: '', 3: ' ', 7: ' / '}
    
def read():
    
    def on_key_release(key): 
        if key == Key.space:
            log_release.append(time())
            log.append(time() - t)
            return False 
        elif key == Key.enter:
            stop.append(True)
            return False

    def on_key_press(key): 
        if key == Key.space: return False 
        elif key == Key.enter:
            return False

    stop = [False]
    log = []
    log_press = []
    log_release = []

    while not stop[-1]:

        with Listener(on_press = on_key_press) as press_listener: 
            press_listener.join()

        t = time()
        log_press.append(t)

        with Listener(on_release = on_key_release) as release_listener: 
            release_listener.join()

    log = [1 if l < 2 else 3 for l in log]
    log_spaces = [a-b for a,b in zip(log_press[1:], log_release)]
    log_spaces = [1 if l < 2 else 7 if l > 4 else 3 for l in log_spaces]
    log_spaces[-1] = 1

    code = [DUR_TO_CODE[l] for l in log]
    sep = [DUR_TO_SEP[l] for l in log_spaces]

    msg = ''.join([''.join(p) for p in zip(code, sep)])
    
    return msg
    

def main():
    print('<dot> hold 1 second\n'
         '<dash> hold 3 seconds\n'
         '<space between parts of the same letter> lift 1 second\n'
         '<space between two letters> lift 3 seconds\n'
         '<space between two words> lift 7 seconds\n'
         '*************************************************************************')
    print('Please use the SPACE key to encode your message.')
    print('Press the ENTER key when the message is completed.')
    print('You may start now.')

    print(read())
    

if __name__ == '__main__':
    main()
