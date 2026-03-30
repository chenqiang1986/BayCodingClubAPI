import json
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request

from lib.image_ai import image_summary, make_story

app = Flask(__name__)

# The front end 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/summary_image', methods=['POST'])
def summary_image():
    print("Process Image Summary")
    images= json.loads(request.data) 
    value = json.dumps(image_summary(images["url"]))
    print(value)
    return value

@app.route('/generate_story', methods=['POST'])
def generate_story():
    image_url_with_desc_list = json.loads(request.data)
    print(image_url_with_desc_list)
    value = json.dumps(make_story(image_url_with_desc_list))
    print(value)
    return value



if __name__ == '__main__':
    app.run(debug=True)