import json
from flask.app import Flask
from flask import request
from pySdk.idToken import idToken
from pySdk.accessToken import accessToken
from flask_cors import CORS
from datetime import timezone
import datetime
app = Flask(__name__)
CORS(app)


@app.route('/',methods=['POST'])
def App():
    
    token = request.data
    objs=json.loads(token)
    token=objs['accessToken']
    #  signature verification

    if not accessToken(token).decodePayload():
        print("signature is invalid")
        return {};
    if not validateAddtionalAttributes(token):
        print("invalid additional attributes")
        return {};
    print(accessToken(token).getUserId());
    print(accessToken(token).decodePayload())
    return accessToken(token).decodePayload();
    

   

def validateAddtionalAttributes(token):
        dt = datetime.datetime.now(timezone.utc)
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        
        if(accessToken(token).getIss()!="https://www.secuuth.io"):
            return False
        if(accessToken(token).getAud()!="***************************"):
            return False;
        if(utc_timestamp-accessToken(token).getExp()>0):
            return False
        
        return True




    