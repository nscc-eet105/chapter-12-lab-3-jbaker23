#My name is Jacob Baker and this is Chapter 12 Lab 3 which I am revising on July 14
import requests

# https://api.openweathermap.org/data/2.5/weather?zip=43512,us&appid=46a1ee1f6ca213ffbdb6d80f5096af86&units=imperial

response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=43512,us&appid=46a1ee1f6ca213ffbdb6d80f5096af86&units=imperial")

if response:
    response_dict=response.json()

    print("The current Weather for", response_dict["name"], "is:")
    print("Conditions:", response_dict["weather"][0]["description"])
    print("Temperature:", response_dict["main"]["temp"],"degrees F")
    print("Feels like:", response_dict["main"]["feels_like"],"degrees F")
    print("Humidity:", response_dict["main"]["humidity"],"%")
    print("Wind Speed:", response_dict["wind"]["speed"],"knots @", response_dict["wind"]["deg"], "degrees")
