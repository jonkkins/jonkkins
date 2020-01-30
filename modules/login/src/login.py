from flask import Flask, request, Response
from jwcrypto import jwt, jwk, jws
from mongo import db
from config import config
import json
import bcrypt
import time

# Essential Instances
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    auto_create_default_user()
    user = db()['users'].find_one({"username": request.form['username'].lower()})
    valid_username = request.form['username'].lower() == user['username'].lower()
    valid_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), user['password']) == user['password']

    if valid_username and valid_password:
        token = jwt.JWT(header={'alg': 'HS256'}, claims={
            'usr': user['username'],
            'iat': int(time.time()),
            'exp': int(time.time() + 900)
        })
        token.make_signed_token(jwk.JWK.from_json(json.dumps(config()['auth']['jwk'])))
        return Response(json.dumps({"msg": "Login success.", "jws": token.serialize()}), mimetype='application/json'), 200
    return Response(json.dumps({"msg": "Invalid username and/or password"}), mimetype='application/json'), 403


@app.route('/verify')
def verify_token():
    try:
        jwt.JWT(jwt=request.form(['token'], key=jwk.JWK.from_json(json.dumps(config()['auth']['jwk']))))
        return Response('{"msg":"Token is valid"}', mimetype='application/json'), 200
    except jws.InvalidJWSSignature:
        return Response('{"msg":"Token is invalid"}', mimetype='application/json'), 403


def auto_create_default_user():
    default_user = db()['users'].find_one({"username": "ghabxph"})
    if not default_user:
        db()['users'].insert_one({"username": "ghabxph", "password": bcrypt.hashpw(b'stonkestpw', bcrypt.gensalt())})
