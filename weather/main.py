import os
from dotenv import load_dotenv
import requests
import json


def main():
    load_dotenv()

    weather_api_key = os.getenv("WEATHER_API_KEY")

    #response = requests.get("http://api.weatherapi.com/v1/current.json?key=" + weather_api_key+ "&q=94568")

    response = requests.post("http://api.weatherapi.com/v1/current.json", data={"key": weather_api_key, "q": "94568"})

    response_json = json.loads(response.content)

    print(json.dumps(response_json, indent=4))
    print(response_json["current"]["condition"])


if __name__ == "__main__":
    main()