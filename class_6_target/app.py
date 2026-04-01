import os
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

# dotenv -f /path/to/.env run python3 app.py
load_dotenv() # load from .env by default in the current directory
    
import json
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL = "gemini-3-flash-preview"
MODEL = "gemini-3.1-flash-lite-preview"
MODEL = "gemini-2.5-flash-lite" 

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


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
        num1 = data['num1']
        num2 = data['num2']
        sum = num1 + num2
        return json.dumps({"sum": sum}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500
    

def data_url_to_google_types(data_url):
    _, media_type, encode_base, content = re.split("data:|;|,", data_url)
    return types.Part.from_bytes(
        mime_type=media_type,
        data=content,
    )


"""
example of input:
[
    {
        "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRg...", 
        "description": "A girl walks into the forest"
    }, 
    {
        "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRg...", 
        "description": "She discovers a magical cabin"
    }
]
"""
def make_story(image_url_with_desc):
    try:
        contents = [
            """
            Based on the input images, and their descriptions, please make up a story.
            Control the output within 100 words.
            """
        ]
        i = 0
        for it in image_url_with_desc:
            i += 1
            contents.append(data_url_to_google_types(it["data_url"]))
            contents.append(f"The {i}-th image's description: " + it["description"])
        
        response = client.models.generate_content(
            model = MODEL,
            contents=contents,
        )
        
        return {
            "story": response.text
        }
    except Exception as e:
        return {
            "story": f"Exception occured: {e}"
        }
        

@app.route('/generate_story', methods=['POST'])
def generate_story():
    image_url_with_desc_list = json.loads(request.data)
    print(image_url_with_desc_list)
    value = json.dumps(make_story(image_url_with_desc_list))
    print(value)
    return value

if __name__ == '__main__':
    app.run(debug=True)