from google import genai
from dotenv import load_dotenv
import os

client = genai.Client()

def enrich_with_suggestion(weather_data):
    results = []
    for weather_piece in weather_data:
        prompt = f"""
            On {weather_piece["date"]}, the weather is {weather_piece["condition"]}, 
            the lowest temperature is {weather_piece["mintemp_c"]},
            and the highest temperature is {weather_piece["maxtemp_c"]},
            please give me the suggestion of what clothes to wear, if I need to bring umbrella etc.
            please keep the answer concise, just summarize one suggestion in one sentence.
        """
        
        response = client.models.generate_content(
            model = "gemini-3-flash-preview",
            contents=prompt
        )
        
        results.append(weather_piece | {"suggestion" : response.text})
        
    return results
