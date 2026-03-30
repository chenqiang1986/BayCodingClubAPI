from dotenv import load_dotenv
try:
    load_dotenv() # load from .env by default in the current directory
    load_dotenv("/etc/secrets/.env")
except Exception as e:
    print(f"Error loading .env file: {e}")
    
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/inc5')
def inc5():
    num = int(request.args.get('num'))
    
    result = num + 5
    return json.dumps({"result": result}), 200


@app.route('/add')
def add():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        
        sum = num1 + num2
        return json.dumps({"sum": sum}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 400


@app.route('/add_post', methods=['POST'])
def add_post():
    try:
        data = json.loads(request.data)
        num1 = data.get('num1')
        num2 = data.get('num2')
        sum = num1 + num2
        return json.dumps({"sum": sum}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500
    

@app.route('/about')
def about():
    return """
         <h1>Hello World!</h1>
         <input type="button" value="Click Me!" onclick="alert('Button Clicked!')">
    """, 200

if __name__ == '__main__':
    app.run(debug=True)