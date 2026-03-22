from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

while True:
    question = input("Enter your question:")
    if question == "exit":
        break
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=question
    )
    
    print(response.text)