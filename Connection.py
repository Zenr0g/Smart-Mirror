from tkinter import *
import requests
from PIL import Image,ImageTk


path_WifiOff = r'E:\Zenpy\Zenvoid\Icons\WifiOff.jpg'
path_WifiOn = r'E:\Zenpy\Zenvoid\Icons\WifiON.jpg'
def CheckWifi(root):
        url='http://www.google.com/'
        timeout=5
        try:
            _ = requests.get(url, timeout=timeout)
            global render
            icon = Image.open(path_WifiOn)
            render = ImageTk.PhotoImage(icon)
            WifiOn = Label(root,image = render,relief = 'solid')
            WifiOn.place(x = 1220,y = 690)
        except requests.ConnectionError:
            icon = Image.open(path_WifiOff)
            render = ImageTk.PhotoImage(icon)
            WifiOn = Label(root,image = render,relief = 'solid')
            WifiOn.place(x = 1220,y = 690)
