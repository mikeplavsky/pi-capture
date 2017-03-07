from flask import Flask, redirect, url_for, request
import json 

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def auth():
    
    s = request.data.decode('utf8')

    print(s)

    res =json.loads(s)
    print(res)

    return "Done"

@app.route('/')
def index():
    return redirect(
            url_for('static', filename='index.html'))
