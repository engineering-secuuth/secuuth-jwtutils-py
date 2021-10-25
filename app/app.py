import json
from flask.app import Flask
from flask import request
from pySdk.idToken import idToken
from pySdk.accessToken import accessToken
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/',methods=['POST'])
def App():
    
    token = request.data
    objs=json.loads(token)
    x=objs['accessToken']
    print(accessToken(x).getUserId());
    print(accessToken(x).decodePayload())
    return accessToken(x).decodePayload();