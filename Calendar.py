from __future__ import print_function
import datetime
from datetime import date
import pickle
from tkinter import *
import os.path
import time
import dateutil.parser
import threading
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def calendarMain(root):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    # print(events_result)
    events = events_result.get('items', [])
    if not events:
        # print('No upcoming events found.')
        pass
        # Custom Code Begins from here
    event_summaries = []
    event_time = []
    event_day = []
    remaining_days = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_summaries.append(event['summary'])
        date = dateutil.parser.parse(start)
        day = date.strftime(r'%d %B')
        event_day.append(day)
        hour = date.strftime('%I')
        minute = date.strftime('%M %p')
        time = f'{hour}:{minute}'
        event_time.append(time)
        day1 = int(date.strftime(r'%d'))
        month = int(date.strftime('%m'))
        year = int(date.strftime('%Y'))

    def writeToJSONFile(data):
        with open('E:\Zenpy\ZenVoid\CalendarJson.json','w') as fp:
            json.dump(data,fp)

    event_data = {}
    event_data['event-name'] = event_summaries
    event_data['event-day'] = event_day
    event_data['event-time'] = event_time
    # event_data['remaining-days-for-event'] = new_date
    writeToJSONFile(event_data)
    # print('calendar')
