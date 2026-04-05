import os
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

# dotenv -f /path/to/.env run python3 app.py
load_dotenv() # load from .env by default in the current directory
    
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, World!", 200


if __name__ == '__main__':
    app.run(debug=True)