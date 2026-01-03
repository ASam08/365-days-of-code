import tkinter as tk
import os
from dotenv import load_dotenv
import requests
import json

def get_weather(location,result_label,entry):
    result_label.config(text="")  

    urlHead = "http://api.weatherapi.com/v1/current.json?"
    apiKey = "key=" + os.getenv("WEATHER_API_KEY")
    urlLocation = "q=" + location
    url = urlHead + apiKey + "&" + urlLocation + "&aqi=no"

    response = requests.get(url)

    data = json.loads(response.text)
    if("error" in data):
        result = (f"Error: {data['error']['message']}")
    else:
        result = (f'Currently in {data["location"]["name"]}, {data["location"]["country"]} it\'s {data["current"]["condition"]["text"].lower()} with a temperature of {data["current"]["temp_c"]}°C.')
 
    entry.delete(0, tk.END)
    result_label.config(text=result,fg="blue")

def on_button_click(result_label,entry):
    location = entry.get()
    get_weather(location,result_label,entry)

def main():
    load_dotenv()

    window = tk.Tk()
    window.title("Weather Report")
    window.geometry("325x150")

    greeting = tk.Label(text="Welcome to the Weather Report App!")
    greeting.grid(row=0, column=0, sticky="n",columnspan=2)

    query = tk.Label(text="Which town or city would you like the current weather for?",justify="center")
    query.grid(row=2, column=0, sticky="n", columnspan=2,pady=5,padx=5)

    entry = tk.Entry() 
    entry.grid(row=3, column=0, sticky="e")
    entry.focus_set()

    result_label = tk.Label(text="",wraplength=300, justify="center")
    result_label.grid(row=6, column=0, sticky="n",pady=10,columnspan=2)


    button = tk.Button(text="Get Weather", command=lambda: on_button_click(result_label,entry))
    button.grid(row=3, column=1, sticky="w", pady=10)    
 

    entry.bind('<Return>', lambda event: on_button_click(result_label,entry))

    window.mainloop()

if __name__ == "__main__":
    main()  