import json

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index_entrance():
    return render_template('index.html'), 200

@app.route('/my_backend', methods=['POST'])
def my_backend():
    my_input = json.loads(request.data)
    
    return json.dumps({
        "sum": my_input["num1"] + my_input["num2"]
    })

app.run(
    host="127.0.0.1",
    port=5000,
)