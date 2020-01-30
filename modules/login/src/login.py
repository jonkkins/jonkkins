from flask import Flask, request, Response
from jwcrypto import jwt, jwk, jws
from lib.mongo import db
from lib.config import config
import json
import bcrypt
import time
import random
import string

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


@app.route('/login-slave', methods=['POST'])
def login_slave():
    auto_create_default_agent()
    query = {"name": request.form['name'].lower()}
    agent = db()['agents'].find_one(query)
    if agent and bcrypt.hashpw(request.form['password'].encode('utf-8'), agent['password']) == agent['password']:
        new_password = ''.join(random.choice(string.letters + string.digits) for i in range(32))
        db()['agents'].update_one(query, {"$set": {"password": bcrypt.hashpw(new_password, bcrypt.gensalt())}})
        token = jwt.JWT(header={'alg': 'HS256'}, claims={
            'usr': agent['name'],
            'iat': int(time.time()),
            'exp': int(time.time() + 900)
        })
        token.make_signed_token(jwk.JWK.from_json(json.dumps(config()['auth']['jwk'])))
        return Response(json.dumps({"msg": " Agent connected successfully.", "jws": token.serialize(), "new_password": new_password}), mimetype='application/json'), 200
    return Response(json.dumps({"msg": "Invalid agent credentials"}), mimetype='application/json'), 403


@app.route('/verify')
def verify_token():
    try:
        jwt.JWT(jwt=request.form(['token'], key=jwk.JWK.from_json(json.dumps(config()['auth']['jwk']))))
        return Response('{"msg":"Token is valid"}', mimetype='application/json'), 200
    except jws.InvalidJWSSignature:
        return Response('{"msg":"Token is invalid"}', mimetype='application/json'), 403


@app.errorhandler(404)
def error_404(e):
    return Response('{"msg": "Error 404. Resource not found."}', mimetype='application/json'), 404


def auto_create_default_user():
    default_user = db()['users'].find_one({"username": "ghabxph"})
    if not default_user:
        db()['users'].insert_one({"username": "ghabxph", "password": bcrypt.hashpw(b'stonkestpw', bcrypt.gensalt())})


def auto_create_default_agent():
    default_agent = db()['agents'].find_one({"name": "first-agent"})
    if not default_agent:
        db()['agents'].insert_one({"name": "first-agent", "password": bcrypt.hashpw(b'stonkestpw', bcrypt.gensalt())})
