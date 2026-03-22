from collections import defaultdict
import os
import requests
import json


def get_weather_from_api(zip_code: str, days: str):
    weather_api_key = os.getenv("WEATHER_API_KEY")

    response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={zip_code}&days={days}")

    if response.status_code != 200:
        print("Error Fetching Weather with Error Code: ", response.status_code)
        return []

    response_json = json.loads(response.content)

    forecast_day_list = response_json["forecast"]["forecastday"]
    result = []
    for forecast_day in forecast_day_list:
        result.append({
            "date": forecast_day['date'],
            "condition": forecast_day['day']['condition']['text'],
            "maxtemp_c": str(forecast_day['day']['maxtemp_c']) + "°C",            
            "mintemp_c": str(forecast_day['day']['mintemp_c']) + "°C",
        })
    
    return result

