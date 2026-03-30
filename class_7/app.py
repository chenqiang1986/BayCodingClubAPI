import json

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index_entrance():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask App</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <input id="clickButton" type="button" value="Click Me!">
        </body>
        <script>
            document.getElementById('clickButton').addEventListener('click', function() {
                alert('Button was clicked!');
            });
        </script>
        </html>
    """, 200