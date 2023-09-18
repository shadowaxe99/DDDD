
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_credentials():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.readonly']
    SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    except Exception as e:
        print(f"Error loading credentials: {e}")

    return creds

def create_event(event_data):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': event_data['summary'],
        'location': event_data['location'],
        'description': event_data['description'],
        'start': {
            'dateTime': event_data['start_time'],
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': event_data['end_time'],
            'timeZone': 'UTC',
        },
        'attendees': event_data['attendees'],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        return event.get('id')
    except Exception as e:
        print(f"Error creating event: {e}")
        return None

def get_emails():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
        messages = results.get('messages', [])
        return messages
    except Exception as e:
        print(f"Error retrieving emails: {e}")
        return None

