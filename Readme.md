# Daily Planner using Google Calendar API

This project consists of two Python scripts that work together to create a working daily plan for weekdays (Monday to Friday) using the Google Calendar API. The scripts allow you to define your table data containing various activities, their start times, and locations, and then automatically create corresponding Google Calendar events for each activity.

Requirements:

    Python 3.x
    Google API Client Library: google-api-python-client
    Google Auth Library: google-auth
    dateutil.parser (typically included with Python)

Instructions:

    gen_creds.py:
        The gen_creds.py script is used for generating and managing the credentials required to access the Google Calendar API.

    Setup:
        Make sure you have the credentials.json file, which contains your Google API credentials.
        The first time you run this script, it will open a web browser and prompt you to log in to your Google account to grant permissions to the application.
        After logging in and granting permission, the script will generate the required token.json file that stores your access and refresh tokens.

    Execution:
        Run the script using the following command:

    python gen_creds.py

    The script will handle the OAuth 2.0 authentication process and generate the necessary credentials for future API calls.

script.py:

    The script.py script contains the table data, including the event names, start times, and locations for each activity. It uses the Google Calendar API to create corresponding events on your Google Calendar.

Setup:

    Before running script.py, ensure you have successfully run gen_creds.py to generate the required token.json file.

Execution:

    Run the script using the following command:

        python script.py

        The script will create Google Calendar events for each activity listed in the table_data variable, recurring every weekday (Monday to Friday) at the specified start times. The events will have a duration of one hour.

Customization:

    You can modify the table_data variable in script.py to define your own daily plan. The format should be: [Event Category, Event Name, Start Time, Location].
    Make sure to use 24-hour format for the start times (e.g., "9:00 am" should be "9:00", "2:30 pm" should be "14:30").

Note:

    The script is designed to work with weekdays (Monday to Friday). If you want to include weekends in the plan, you'll need to modify the recurrence rule in the create_google_calendar_event function in script.py.

Disclaimer:

    This project uses the Google Calendar API to access and modify your Google Calendar events. Please review the code carefully, as it will have access to your calendar and is capable of creating, modifying, and deleting events. Ensure that you trust the source and the code before running it on your system.
