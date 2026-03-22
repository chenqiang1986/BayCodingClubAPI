import json
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request
from address.lib import normalize_zip_code
from wearing.lib import enrich_with_suggestion
from weather.lib import get_weather_from_api

app = Flask(__name__)

# The front end 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_zip_code', methods=['GET'])
def get_zip_code():
    state = request.args.get("state")    
    city = request.args.get("city")
    zip_code = request.args.get("zip_code")
    return json.dumps({"zip_code": normalize_zip_code(state, city, zip_code)})


@app.route('/get_weather', methods=['GET'])
def get_weather():
    zip_code = request.args.get("zip_code")
    days = request.args.get("days")
    return json.dumps(get_weather_from_api(zip_code, days))

@app.route('/get_wearing_suggestion', methods=['POST'])
def get_wearing_suggestion():
    weather_data = json.loads(request.data)
    return json.dumps(enrich_with_suggestion(weather_data))

    

if __name__ == '__main__':
    app.run(debug=True)