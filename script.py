import os
import datetime
import dateutil.parser
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Define your table data here (event name, start time, location)
table_data = [
    ["Hygiene", "Make bed", "9 am", "Bedroom"],
    ["Hygiene", "Brush teeth", "9.05 am", "Bathroom"],
    ["Hygiene", "Take bath", "9.45 am", "Bathroom"],
    ["Work", "Go to office", "10.15 am", "Hustlehub"],
    ["Work", "Morning session", "10.30 am", "Hustlehub"],
    ["Work", "Afternoon session", "2.30 pm", "Hustlehub"],
    ["Workout and health", "Cycling", "6 pm", "Living room"],
    ["Workout and health", "Push ups (30)", "6.45 pm", "Living room"],
    ["Workout and health", "Abs: 2 workouts", "7 pm", "Living room"],
    ["Workout and health", "Cooking", "8 pm", "Living room"],
    ["Relationships", "Text 1 friend and 1 family", "8.30 pm", "Bedroom"],
    ["Dev growth", "Leetcode", "9 pm", "Living room"],
    ["Dev growth", "Course or starter project", "10 pm", "Living room"],
    ["Podcast(Optional)", "Notes and match", "12 am", "Living room"],
    ["Hobbies(Optional)", "Learn musical instrument", "12 am", "Bedroom"],
    ["Finances and progress tracking", "Read and write Reflect", "1 am", "Bedroom"],
    ["Finances and progress tracking", "Music or random podcast and sleep", "2.30 am", "Bedroom"],
]

def create_google_calendar_event(service, event_name, start_time, location):
    start = dateutil.parser.parse(start_time).isoformat()
    end = (dateutil.parser.parse(start_time) + datetime.timedelta(hours=1)).isoformat()  # Assume 1-hour duration

    event = {
        'summary': event_name,
        'start': {'dateTime': start, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end, 'timeZone': 'Asia/Kolkata'},
        'location': location,
        'recurrence': ['RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR'],  # Recur on weekdays (Monday to Friday)
    }

    service.events().insert(calendarId='primary', body=event).execute()

def main():
    # Set up OAuth 2.0 credentials using the refresh token
    scopes = ['https://www.googleapis.com/auth/calendar']

    creds = Credentials.from_authorized_user_file('token.json', scopes=scopes)

    service = build('calendar', 'v3', credentials=creds)

    for entry in table_data:
        event_category, event_name, start_time, location = entry
        create_google_calendar_event(service, f"{event_category}: {event_name}", start_time, location)

if __name__ == "__main__":
    main()

