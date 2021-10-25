

import json
from flask.app import Flask

from flask import request

from pySdk.idToken import idToken
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


@app.route('/',methods=['POST'])
def hello_world():
    #token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3OTQyZmJmMC1mOTk2LTRiODctYTE2My0yNjlmNDA3MzZlM2IiLCJhdWQiOiI5MmFkYWFjZC1kMjUyLTQ3NTctOWFjMi0yZDQ4ZDdlYzM3YmIiLCJpc3MiOiJodHRwczovL3d3dy5zZWN1dXRoLmlvIiwiZXhwIjoxNjM0OTYzNDc3Mjc3LCJqdGkiOiIzYTljMDk0NS02NmFkLTQ5ZTgtOGRjZS0xY2FkNDYyYmE2MjEiLCJ0eXAiOiJBY2Nlc3NfdG9rZW4iLCJzaWduSW5Nb2RlIjowLCJ1c2VySWQiOiI5OXJhamFtaTExQGdtYWlsLmNvbSIsInNjb3BlIjoiYWNjZXNzIiwiaWF0IjoxNjM0OTU5ODc3fQ.FV7YfbH6nn9BxEn0IGGa0f5Ru1C0qlEQ9VOiDBL341XlRO_sKArdhUcDTFJAz7mNyAwW49bdfVqvbTsnjmVKAau2fb9tTBg6qF9l9CuplZpCMk65nrS6wkQaj3o8z_NEeVCdHfNFJZavpxaNMKD7wX_8pC5YMMgz2tk91tuC0xPjr1Xaw7MJSEB_eOStg1LK8fs6kzsKN10iJYTskn2R0k_t40UjCp5Ca6hG8BoofCbqbI6C_8cPEDjabznJZAjpj6sTyY5_GMD2_VmAPmaf5gNJcje1DQTp_kUlHMwToq4FbsuLwm8JjsWkgz7YaGVnUfBkxggzWl4lL_M-BgwWYQ"
    data = request.data
    objs=json.loads(data)
    x=objs['idToken']
    print(x)
    print(idToken(x).getUserId());
    return idToken(x).getUserId();