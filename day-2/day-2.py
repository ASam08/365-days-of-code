import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("RAPIDAPI_KEY")

url = "https://flight-fare-search.p.rapidapi.com/v2/flights/"
origin = input("Enter origin airport code (e.g. LHR): ")
destination = input("Enter destination airport code (e.g. DXB): ")  
travel_date = input("Enter travel date (YYYY-MM-DD): ")
adults = input("Enter number of adults: ")
children = input("Enter number of children: ")
infants = input("Enter number of infants: ")
class_type = input("Enter travel class type (economy, business, first): ")

adults = int(adults or 0)
children = int(children or 0)
infants = int(infants or 0)

querystring = {"from":origin,"to":destination,"date":travel_date,"adult":adults,"child":children,"infant":infants,"type":class_type,"currency":"NZD"}

headers = {"x-rapidapi-host": "flight-fare-search.p.rapidapi.com","x-rapidapi-key": api_key}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

totalFlights = len(data['results'])
sortedByPrice = sorted(data['results'], key=lambda x: x['totals']['total'])
sortedByDuration = sorted(data['results'], key=lambda x: x['duration']['value'])
departureAirport = data['results'][0]['departureAirport']['label']
arrivalAirport = data['results'][0]['arrivalAirport']['label']
passengers = [f"{adults} Adult" if adults and int(adults) == 1 else "" if int(adults) == 0 else f"{adults} Adults" if adults else "",
              f"{children} Child" if children and int(children) == 1 else "" if int(children) == 0 else f"{children} Children" if children else "",
              f"{infants} Infant" if infants and int(infants) == 1 else "" if int(infants) == 0 else f"{infants} Infants" if infants else ""]
filtered_passengers = [p for p in passengers if p]
passengers = ", ".join(filtered_passengers)
passengers = " and".join(passengers.rsplit(",", 1))
print(f'{totalFlights} flights found travelling between {departureAirport} and {arrivalAirport} on {data["searchData"]["date"]} for {passengers}.')
print(f'The cheapest flight is ${sortedByPrice[0]["totals"]["total"]:.2f}, flying on {sortedByPrice[0]["flight_name"]} with a total flight time of {sortedByPrice[0]["duration"]["text"]}.')
print(f'The fastest flight is ${sortedByDuration[0]["totals"]["total"]:.2f}, flying on {sortedByDuration[0]["flight_name"]} with a total flight time of {sortedByDuration[0]["duration"]["text"]}.')
