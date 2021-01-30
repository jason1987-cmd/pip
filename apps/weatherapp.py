# Weather app in Python using openweathermap API

import requests

def weather():
    
    city = input("Enter city name :")
    API = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=959b696984280a9e3dcb2c071fd76f4d".format(city)
    jsonData = requests.get(API).json()

    mainweather = jsonData['weather'][0]['main']
    description = jsonData['weather'][0]['description']
    temperature = jsonData['main']['temp']
    humidity = jsonData['main']['humidity']
    
    print(mainweather)
    print(description)
    print(temperature)
    print(humidity)

weather()