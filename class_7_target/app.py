import json

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index_entrance():
    return render_template('index.html'), 200


app.run(
    host="127.0.0.1",
    port=5000,
)