import time
import datetime
import threading
import requests
from pyowm import *
from DateTime import *
from tkinter import *
from WeatherData import *
from CalendarData import *
from WeatherIcons import *
from Calendar import *
import sys
import urllib3
import socket
import httplib2
from tkinter import _tkinter
from CalendarData import *
import google.auth.transport


global mainFrame
mainFrame = Tk()
mainFrame.attributes('-fullscreen',True)
mainFrame.configure(bg = 'black')
print('>-- Checking for Internet Connection...')

#  ''' ================================================== '''
def refresher_function():
    while True:
        url='http://www.google.com/'
        timeout=5
        try:
            _ = requests.get(url, timeout=timeout)
            calendarMain(mainFrame)
            mainCalendarData(mainFrame)
            weatherdataMain(mainFrame)
            # print('main')
        except requests.ConnectionError:
            pass
        # mainFrame.update_idletasks()
#  ''' ================================================== '''

weatherdataMain(mainFrame)
mainCalendarData(mainFrame)
dateTimeMain(mainFrame)
weatherIconsMain(mainFrame)

#   ''' ================================================= '''
try:
    if weatherdataMain.Connected_to_Internet == True:
        print('>-- Internet Connected...')
except AttributeError:
    pass
#    ''' ================================================= '''

time.sleep(0.3)
print('>-- Processing files...')
time.sleep(0.5)
print('>-- Starting...')


#   ''' ================================================= '''

try:
    thread = threading.Thread(target = refresher_function)
    thread.daemon = True
    thread.start()

except (httplib2.ServerNotFoundError,google.auth.exceptions.TransportError,RuntimeError,
        pyowm.exceptions.api_call_error.APICallTimeoutError,_tkinter.TclError,
        requests.exceptions.ReadTimeout):
    pass

#   ''' ================================================== '''
mainFrame.mainloop()
