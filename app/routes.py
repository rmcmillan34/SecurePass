from flask import render_template
from app import app
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

    if symbols == False:
        scope = string.ascii_letters + string.digits
    else:
        scope = string.ascii_letters + string.digits + SYMBOLS
    for i in range(num_chars):
        password = password + scope[random.randint(0, len(scope))]

    return password

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='SecurePass', password=generate_password())
