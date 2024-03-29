'''
Secure Pass is a secure password generator that will generate a 15 character
password with symbols.
TODO implement keyword arguments to enable user specified password length, and
the ability to not use symbols in returned password (argparse).

'''

import string
import random


SYMBOLS = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\''


def generate_password(num_chars=15, symbols=True):
    '''Return secure password string of length num_chars characters.
    Keyword arguments:
    num_chars -- length of password to be generated (default 15)
    symbols   -- bool to include ascii symbols      (default True)
    '''
    password = ''

    if not symbols:
        scope = string.ascii_letters + string.digits
    else:
        scope = string.ascii_letters + string.digits + SYMBOLS
    for i in range(num_chars):
        password = password + scope[random.randint(0, len(scope))]

    return password


def main():
    '''Main method. calls generate password method and prints returned string.
    '''
    print(generate_password())


if __name__ == '__main__':
    main()
