import json

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index_entrance():
    return render_template("index.html"), 200

@app.route('/my_backend', methods=['POST'])
def my_backend():
    my_input = json.loads(request.data)
    
    print(my_input)
    
    if isinstance(my_input["num1"], int) and isinstance(my_input["num2"], int):
        return json.dumps({
            "sum": my_input["num1"] + my_input["num2"]
        })
    else:
        return json.dumps({
            "error": "Input is not integer"
        })
    
app.run(debug=True)