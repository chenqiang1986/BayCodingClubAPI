import base64
import os

from google import genai
from google.genai import types
import dotenv

dotenv.load_dotenv()

with open('/Users/qiangchen/Downloads/xab.jpg', 'rb') as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    image_data_url = f"data:image/jpeg;base64,{image_b64}"

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

"""
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Part.from_bytes(
            mime_type="image/jpeg",
            data=image_b64
        ),
        'Caption this image.'
    ]
)


response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

"""

chat = client.chats.create(model = 'gemini-3-flash-preview')
response = chat.send_message([
    types.Part.from_bytes(
            mime_type="image/jpeg",
            data=image_b64
        ),
    'Make a title for the image. Keep it short and simple.',
])

print(response.text)

response = chat.send_message(
    "Let's include the color of the duck into the title."
)

print(response.text)