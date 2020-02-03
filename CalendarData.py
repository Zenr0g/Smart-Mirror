from tkinter import *
import json
from Calendar import *
import time
import threading
import os

def mainCalendarData(root):

    # print('thread')
#  ''' ========================================================= '''
    def getJSONFile(FileNameAndPath):
        with open(FileNameAndPath,'r') as rp:
            return json.load(rp)

    def get_data():
        global readcalendar
        if os.path.abspath('CalendarJson.json'):
            readcalendar = getJSONFile('E:\Zenpy\ZenVoid\CalendarJson.json')
            root.after(500,get_data)
    get_data()

# '''========================================================================================== '''
    def getCalendarData(root):
        global breakpoint2
        breaker = '. ' * 70

        breakpoint1 = Label(root,bg = 'black', fg = 'white',text = str(breaker))
        breakpoint1.place(x = 20, y = 470)
        breakpoint2 = Label(root, bg = 'black', fg = 'white',text = str(breaker))


        if len(readcalendar['event-name']) == 3:
            breakpoint2.place(x = 20, y = 510)
        else:
            breakpoint2.pack_forget()

        toplabel = Label(root,fg = 'white', bg = 'black', text = 'Upcoming events:',
                                                          font = ('Nova Flat', 24))

        try:
            daylabel = Label(root,fg = 'white', bg = 'black', font = ('Nova Flat',16),
                                                              text = readcalendar['event-day'][0])
            daylabel1 = Label(root,fg = 'white', bg = 'black', font = ('Nova Flat',16),
                                                              text = readcalendar['event-day'][1])
            daylabel2 = Label(root,fg = 'white', bg = 'black', font = ('Nova Flat',16),
                                                              text = readcalendar['event-day'][2])
        except IndexError:
            pass

        try:
            event_namelabel = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-name'][0])
            event_namelabel1 = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-name'][1])
            event_namelabel2 = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-name'][2])
        except IndexError:
            pass

        try:
            event_timelabel = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-time'][0])
            event_timelabel1 = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-time'][1])
            event_timelabel2 = Label(root,fg = 'white', bg = 'black',font = ('Nova Flat',16),
                                                              text = readcalendar['event-time'][2])
        except IndexError:
            pass

# '''================================================================================================ '''
        try:
            toplabel.place(x = 20, y = 400)

            daylabel.place(x = 180, y = 450)
            daylabel1.place(x = 180,y = 490)
            daylabel2.place(x = 180,y = 530)

        except NameError:
            pass

        try:
            event_namelabel.place(x = 20,y = 450)
            event_namelabel1.place(x = 20,y = 490)
            event_namelabel2.place(x = 20,y = 530)

        except NameError:
            pass

        try:
            event_timelabel.place(x = 330,y = 450)
            event_timelabel1.place(x = 330,y = 490)
            event_timelabel2.place(x = 330,y = 530)

        except NameError:
            pass

    getCalendarData(root)
    root.after(500,getCalendarData(root))
#   ''' ================================================================= '''
