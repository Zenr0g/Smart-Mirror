import datetime
import time
from tkinter import *
import sys


def dateTimeMain(root):

#  ''' ======================================== '''
    def tick():
        time_str = time.strftime('%I %M')
        clock.config(text = time_str)
        clock.after(200,tick)

#  ''' ========================================= '''
    date = datetime.datetime.now()
    dayname = date.strftime('%A')
    day = date.strftime(r'%d')
    month = date.strftime('%b')
    year = date.strftime('%Y')
    minutes = time.strftime('%M')


#  ''' =================================================================================== '''
    if dayname == 'Monday'or'Sunday':
        lines = '. ' * 26
    elif dayname == 'Friday':
        lines = '. ' * 15
    elif dayname == 'Tuesday':
        lines = '. ' * 32
    elif dayname == 'Thursday' or 'Saturday':
        lines = '. ' * 35
    elif dayname == 'Wednesday':
        lines = '. ' * 37

    underlines = Label(root,bg = 'black', fg = 'white', text = str(lines))

    clock = Label(root,bg = 'black', fg ='white', font = ('Universe',120))
    daynamelabel = Label(root,bg = 'black', fg = 'white' ,font = ('Earth Orbiter Title',20),
                                                        text = str(dayname))
    daylabel = Label(root,bg = 'black', fg = 'white',font = ('Universe',28,'bold'),
                                                        text = str(day))
    monthlabel = Label(root,bg = 'black', fg = 'white',font = ('Earth Orbiter Title',30),
                                                        text = str(month))
    yearlabel = Label(root,bg = 'black', fg = 'white',font = ('Universe',28,'bold'),
                                                        text = str(year))
# ''' ====================================================================================== '''

    clock.place(x = 20,y = 10)
    daynamelabel.place(x = 100,y = 222)
    underlines.place(x = 100, y = 242)
    daylabel.place(x = 280,y = 262)
    monthlabel.place(x = 150,y = 272)
    yearlabel.place(x = 360,y = 262)

    tick()
