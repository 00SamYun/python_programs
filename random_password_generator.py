import string
from random import randint, randrange, choice, sample


SYMBOLS = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
LCASE = string.ascii_lowercase
UCASE = string.ascii_uppercase


def generate_pwd(min_len=15, max_len=30):
    '''
    generates a strong password string
    minimum 15 characters long by default 
    includes uppercase and lowercasde letters, numbers and symbols 
    '''
    
    pwd_len = random.randint(min_len, max_len)
    num_count = random.randrange(1, pwd_len//2.5)
    sym_count = random.randrange(1, pwd_len//2.5)
    word_count = pwd_len - num_count - sym_count
    lcase_count = random.randrange(1, word_count-1)
    ucase_count = word_count - lcase_count

    nums = [str(random.randint(0, 9)) for i in range(num_count)]
    syms = [random.choice(SYMBOLS) for i in range(sym_count)]
    lcase = [random.choice(LCASE) for i in range(lcase_count)]
    ucase = [random.choice(UCASE) for i in range(ucase_count)] 


    pwd = nums + syms + lcase + ucase
    pwd = ''.join(random.sample(pwd, len(pwd)))
    
    return pwd
