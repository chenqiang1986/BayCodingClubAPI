from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/process', methods=['POST'])
def process():
    print("Args", request.args)
    print("Data",request.data, len(request.data))
    return '{"status": "success"}'

if __name__ == '__main__':
    app.run(debug=True)