from flask import Flask, request
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests

app = Flask(__name__)

# Load Google API credentials
credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
service = build('calendar', 'v3', credentials=credentials)

# Load Zoom API credentials
zoom_api_key = 'your_zoom_api_key'
zoom_api_secret = 'your_zoom_api_secret'

@app.route('/schedule-meeting', methods=['POST'])
def schedule_meeting():
    data = request.get_json()

    # Extract meeting details from request data
    meeting_title = data['title']
    start_time = data['start_time']
    end_time = data['end_time']
    attendees = data['attendees']

    # Create Zoom meeting
    zoom_meeting_id = create_zoom_meeting(meeting_title, start_time, end_time, attendees)

    # Create Google Calendar event
    create_calendar_event(meeting_title, start_time, end_time, attendees, zoom_meeting_id)

    return 'Meeting scheduled successfully'

def create_zoom_meeting(title, start_time, end_time, attendees):
    # Create Zoom meeting using Zoom API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {zoom_api_key} {zoom_api_secret}'
    }
    data = {
        'topic': title,
        'start_time': start_time,
        'end_time': end_time,
        'settings': {
            'host_video': True,
            'participant_video': True,
            'join_before_host': True,
            'mute_upon_entry': False,
            'approval_type': 2,
            'registration_type': 1,
            'registrants_email_notification': True
        },
        'attendees': [{'email': attendee} for attendee in attendees]
    }
    response = requests.post('https://api.zoom.us/v2/users/me/meetings', headers=headers, json=data)
    response_data = response.json()
    return response_data['id']

def create_calendar_event(title, start_time, end_time, attendees, zoom_meeting_id):
    # Create Google Calendar event using Google Calendar API
    event = {
        'summary': title,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
        'attendees': [{'email': attendee} for attendee in attendees],
        'conferenceData': {
            'createRequest': {
                'requestId': zoom_meeting_id,
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'
                }
            }
        }
    }
    service.events().insert(calendarId='primary', body=event).execute()

if __name__ == '__main__':
    app.run()