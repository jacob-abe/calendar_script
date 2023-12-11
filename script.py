import os
import datetime
import dateutil.parser
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Define your table data here (event name, start time, location)
table_data = [
    ["Morning Routine", "Wake up", "8 am", "Bedroom"],
    ["Work", "Go to office", "9 am", "Hustlehub"],
    ["Lunch", "Come home for lunch", "1 pm", "Home"],
    ["Work", "Office", "2 pm", "Hustlehub"],
    [
        "Free Time",
        "Consume supplements and get ready for gym. Feed pets",
        "5 pm",
        "Living room",
    ],
    ["Fitness", "CULT", "6 pm", "Gym"],
    ["Free Time", "Home chilling", "7 pm", "Living room"],
    ["Free Time", "Dinner and calls", "8 pm", "Bedroom"],
    ["Learning", "Leetcode+Video editing", "9 pm", "Living room"],
    ["Fitness", "Cycling", "11 pm", "HSR"],
    ["Project/Podcast", "Project/Podcast", "12 am", "Living room"],
    ["Project/Podcast", "Project/Podcast", "1 am", "Living room"],
    ["Finances", "Tally up finances and podcast", "2 am", "Bedroom"],
    ["Sleep", "Sleep", "2 am", "Bedroom"],
]


def create_google_calendar_event(service, event_name, start_time, location):
    start = dateutil.parser.parse(start_time).isoformat()
    end = (
        dateutil.parser.parse(start_time) + datetime.timedelta(hours=1)
    ).isoformat()  # Assume 1-hour duration

    event = {
        "summary": event_name,
        "start": {"dateTime": start, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end, "timeZone": "Asia/Kolkata"},
        "location": location,
        "recurrence": [
            "RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
        ],  # Recur on weekdays (Monday to Friday)
    }

    service.events().insert(calendarId="primary", body=event).execute()


def main():
    # Set up OAuth 2.0 credentials using the refresh token
    scopes = ["https://www.googleapis.com/auth/calendar"]

    creds = Credentials.from_authorized_user_file("token.json", scopes=scopes)

    service = build("calendar", "v3", credentials=creds)

    for entry in table_data:
        event_category, event_name, start_time, location = entry
        create_google_calendar_event(
            service, f"{event_category}: {event_name}", start_time, location
        )


if __name__ == "__main__":
    main()
