import json
from typing import Any
import requests

"""
Read a string from keyboard, interpret it as a json object, print the "name" and "dob" fields of that json object.

Example:

#input
  {"name": "Emma", "dob": "2000-1-1"}
#Output
  Emma
  2000-1-1

#input
  {"name": "George", "dob": "2002-1-1"}
#Output
  George
  2002-1-1

"""
def main():    
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    print(response.content)

if __name__ == "__main__":
    main()