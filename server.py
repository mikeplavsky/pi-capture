from flask import Flask, redirect, url_for, request
import json 

from oauth2client import client

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def auth():
    
    s = request.data.decode('utf8')

    print(s)

    res =json.loads(s)
    print(res)

    creds = client.credentials_from_clientsecrets_and_code(
            "./client_secret.json",
            
            [   'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/drive.appdata',
                'profile', 
                'email'],

            res["code"])

    tokens = creds.to_json()
    print(tokens)

    with open("tokens.json","w") as f:
        print(tokens, file=f)

    return "Done"

@app.route('/')
def index():
    return redirect(
            url_for('static', filename='index.html'))
