from collections import defaultdict
import os
from dotenv import load_dotenv
import requests
import json

def get_condition_breakdown(forecast_day):
    condition_breakdown = defaultdict(lambda: 0)

    for forecast_hour in forecast_day["hour"]:
        condition = forecast_hour["condition"]["text"]
        condition_breakdown[condition] += 1

    return condition_breakdown

def print_condition_breakdown(condition_breakdown):
    print("Condition Breakdown:")
    for condition, count in condition_breakdown.items():
        print(f"  {condition}: {count} hours")

def main():
    load_dotenv()
    weather_api_key = os.getenv("WEATHER_API_KEY")

    location = input("Enter a location (e.g. city name or zip code): ")
    day_count = input("Enter the number of days to forecast (1-14): ")

    response = requests.post("http://api.weatherapi.com/v1/forecast.json", data={"key": weather_api_key, "q": location, "days": day_count})

    if response.status_code != 200:
        print("Error Fetching Weather with Error Code: ", response.status_code)
        return

    response_json = json.loads(response.content)

    forecast_day_list = response_json["forecast"]["forecastday"]
    for forecast_day in forecast_day_list:
        print(f"Date: {forecast_day['date']}")
        print(f"Max Temp: {forecast_day['day']['maxtemp_c']}°C")
        print(f"Min Temp: {forecast_day['day']['mintemp_c']}°C")
        print(f"Condition: {forecast_day['day']['condition']['text']}")

        condition_breakdown = get_condition_breakdown(forecast_day)
        print_condition_breakdown(condition_breakdown)

        print("")


if __name__ == "__main__":
    main()