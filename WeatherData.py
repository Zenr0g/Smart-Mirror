import os
import pyowm           # Module for calling the API
import requests
import time
from tkinter import *
import json
from Calendar import *
from PIL import Image
from PIL import ImageTk
from WeatherIcons import *

def weatherdataMain(root):

#  ''' =========================================================== '''
    def writeToJSONFile(data):
        with open('E:\Zenpy\ZenVoid\WeatherJson.json','w') as fp:
            json.dump(data,fp)


    def getJSONFIle():
        with open('E:\Zenpy\ZenVoid\WeatherJson.json','r') as rp:
            return json.load(rp)

#  ''' ============================================================================ '''
    def check_internet():
        global Connected_to_Internet

        url='http://www.openweathermap.com/'
        timeout=5
        try:
            _ = requests.get(url, timeout=timeout)
            degree_sign = u'\N{DEGREE SIGN}'
            owm = pyowm.OWM('...') # Your API key
            observation = owm.weather_at_place('Mumbai, IN') # Location
            weather = observation.get_weather()
            temperature_data = int(weather.get_temperature('celsius')['temp'])
            temperature = f'{temperature_data}{degree_sign}{" C"}'  # The Temperature
            weather_status = weather.get_status()   # The weather status

            weather_data = {}
            weather_data['temperature'] = temperature
            weather_data['weather-status'] = weather_status
            writeToJSONFile(weather_data)
            weatherdataMain.Connected_to_Internet = True

            # print('weather')

        except requests.ConnectionError:
            time.sleep(0.3)
            print('>-- Internet Connection Failed...')
            time.sleep(0.3)
            print('>-- Working offline...')
        return False

    check_internet()

#  ''' ============================================================================== '''
    weatherJson = getJSONFIle()
    if weatherJson['weather-status'] == 'Thunderstorm':
        statuslabel.place(x = 990, y = 180)

    temperaturelabel = Label(root,fg = 'white', bg = 'black', font = ('Universe',90),
                                                                text = weatherJson['temperature'])
    statuslabel = Label(root,fg = 'white', bg = 'black',padx = 50 ,font = ('Earth Orbiter Title',30),
                                                                text = weatherJson['weather-status'])

    temperaturelabel.place(x = 1000, y =10)
    statuslabel.place(x = 1020,y = 180)
