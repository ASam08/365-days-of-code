import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

location = input("Which town or city would you like the current weather for? ")
urlHead = "http://api.weatherapi.com/v1/current.json?"
apiKey = "key=" + os.getenv("WEATHER_API_KEY")
urlLocation = "q=" + location
url = urlHead + apiKey + "&" + urlLocation + "&aqi=no"

response = requests.get(url)
#print(response.json())

data = json.loads(response.text)
if("error" in data):
    print(f"Error: {data['error']['message']}")
else:
    print(f'Currently in {data["location"]["name"]}, {data["location"]["country"]} it\'s {data["current"]["condition"]["text"].lower()} with a temperature of {data["current"]["temp_c"]}°C.')
