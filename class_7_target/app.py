import json

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index_entrance():
    return render_template('index.html'), 200