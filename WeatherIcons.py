from tkinter import *
from PIL import Image
from PIL import ImageTk
import json
from WeatherData import *
import time


def weatherIconsMain(root):

#  ''' =============================================================== '''
    def getJsonFile(FileNameAnaPath):
        with open(FileNameAnaPath,'r') as rp:
            return json.load(rp)


    weatherStatus = getJsonFile('E:\Zenpy\ZenVoid\WeatherJson.json')
    time_today = time.strftime('%H')
#  ''' =============================================================== '''
    # Path of all the icons in the Icon2 Folder
    path_rain = r'E:\Zenpy\ZenVoid\Icons2\Rain.jpg'
    # path_night_rain = r'E:\Zenpy\ZenVoid\Icons\NightRain.jpg'
    path_night = r'E:\Zenpy\ZenVoid\Icons2\Night.jpg'
    path_clear = r'E:\Zenpy\ZenVoid\Icons2\Clear.jpg'
    path_smoke = r'E:\Zenpy\ZenVoid\Icons2\Smoke.jpg'
    path_clouds = r'E:\Zenpy\ZenVoid\Icons2\clouds.jpg'
    # path_cloud = r'E:\Zenpy\ZenVoid\Icons\Cloud.jpg'
    path_snow = r'E:\Zenpy\ZenVoid\Icons2\Snow.jpg'
    path_morning = r'E:\Zenpy\ZenVoid\Icons2\Morning.jpg'
    # path_sunset = r'E:\Zenpy\ZenVoid\Icons\Sunset.jpg'
    path_thunderstorm = r'E:\Zenpy\ZenVoid\Icons2\Thunderstorms.jpg'
    # path_very_morning = r'E:\Zenpy\ZenVoid\Icons\Verymorning.jpg'
    # path_deep_night = r'E:\Zenpy\ZenVoid\Icons\DeepNight.jpg'

#  ''' ================================================================= '''
    def iconPlacer(path,root):
        global render
        icon = Image.open(path)
        render = ImageTk.PhotoImage(icon)
        label = Label(root,image = render,relief = 'solid')
        label.place(x = 890,y = 50)
#  ''' =============================================================================================== '''

    """ --------- Conditions of each weather icon respective to the current weather status ---------"""

    """ Conditions for normal weather """

    if(int(time_today) >= 1 < 3 and (weatherStatus['weather-status'] == 'Haze' or 'Clear')):
        iconPlacer(path_morning,root)
    if(int(time_today) >= 3 < 10 and (weatherStatus['weather-status'] == 'Haze' or 'Clear')):
        iconPlacer(path_morning,root)
    if(int(time_today) >= 10 < 18 and (weatherStatus['weather-status'] == 'Haze' or 'Clear')):
        iconPlacer(path_clear,root)
    if(int(time_today) >=18 < 20 and (weatherStatus['weather-status'] == 'Haze' or 'CLear')):
        iconPlacer(path_night,root)
    if(int(time_today) >= 20 < 22 and (weatherStatus['weather-status'] == 'Haze' or 'Clear')):
        iconPlacer(path_night,root)
    if(int(time_today) >= 24 and (weatherStatus['weather-status'] == 'Haze' or 'Clear')):
        iconPlacer(path_night,root)


#  ''' ==================================================================================================== '''
    """ Conditions for Rainy weather """
    if(int(time_today) >= 1 < 18 and (weatherStatus['weather-status'] == 'Rain')):
        iconPlacer(path_rain,root)
    if(int(time_today) >=18 <24 and (weatherStatus['weather-status'] == 'Rain')):
        iconPlacer(path_rain,root)


#  ''' ==================================================================================================== '''
    """ Conditions for Smoke """
    if(int(time_today) >= 1 < 12 and weatherStatus['weather-status'] == 'Smoke'):
        iconPlacer(path_morning,root)
    if(int(time_today) >= 12 < 18 and weatherStatus['weather-status'] == 'Smoke'):
        iconPlacer(path_smoke,root)
    if(int(time_today) >= 18 < 20 and weatherStatus['weather-status'] == 'Smoke'):
        iconPlacer(path_night,root)
    if(int(time_today) >= 20 < 24 and weatherStatus['weather-status'] == 'Smoke'):
        iconPlacer(path_night,root)


#  ''' ==================================================================================================== '''
    """ Condition for Thunderstorm """
    if(int(time_today) >= 1 < 24 and weatherStatus['weather-status'] == 'Thunderstorm'):
        iconPlacer(path_thunderstorm,root)
