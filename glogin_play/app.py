import json

from flask import Flask, render_template, request

from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID='1003730491521-2ln1uac6mrr7m1e4g73g9vni2al14ulg.apps.googleusercontent.com'

app = Flask(__name__)


@app.route('/')
def index_entrance():
    return render_template('index.html'), 200

@app.route('/login', methods=['POST'])
def login():
    print(request.data)
    
    login_obj = json.loads(request.data)
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(login_obj["token"], requests.Request(), CLIENT_ID)

        # ID token is valid. Get the user's Google Account ID and email.
        userid = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name')
        picture = idinfo.get('picture')

        print(f"Hello, {name}! Your email is {email}. Your user id is {userid}. Your picture is {picture}")
        
        return json.dumps({"email": email}), 200

    except ValueError:
        # Invalid token
        return "Invalid token", 400


app.run(
    host="127.0.0.1",
    port=5000,
)

