from flask import Flask
from flask import request
import bcrypt

app = Flask(__name__)

# Of course, just a test code.
username = 'ghabxph'

# Password: stonkestpw
password = b'$2b$12$Uc7LQULxOIJEkoGmSGzmPeMY1wNYgw9Upk2EZ3OTyeNA2VUIO6kuG'


@app.route('/login', methods=['POST'])
def hello_world():
    valid_username = request.form['username'].lower() == username.lower()
    valid_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), password) == password
    if valid_username and valid_password:
        return 'valid username and password heh'
    return 'Invalid username and/or password'
