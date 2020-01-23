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

"""
Things to do:
  Reference: https://jwcrypto.readthedocs.io/en/latest/jwt.html
 -- Once username and password matches the database (for now we put it on a variable),
    then what we're going to do next is to generate a JWT that:
      - Claims that 'you' are the logged-in user
      - Kindly see JWT's standard claim. I think the standard claims are
        just enough. No need to think of a customized claim
      - Sign the jwt token, and create:
        {'jwt': '<jwt here'}

-- On the front side:
    - Once we receive the valid login jwt, we must store it somewhere.
    - And then, on every request we made, put the jwt on Authorization: Bearer <jwt>

-- Lastly,
    - Perform a check on header. It'll be in the middleware of every application that
      requires logged-in user.
    - Once the claim are determined to be correct, we can just use the data written here.
      No need to get the data from database, since it is signed, then it is less likely
      to be manipulated
    - We can consider adding another layer (encryption), thus, making it JWE (Json Web
      Token Encrypted)
"""