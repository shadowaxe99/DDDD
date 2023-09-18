from flask import Flask, request
from utils.google_api import GoogleAPI
from utils.zoom_api import ZoomAPI

app = Flask(__name__)

@app.route('/schedule-meeting', methods=['POST'])
def schedule_meeting():
    # Get meeting details from request
    meeting_title = request.json['title']
    meeting_date = request.json['date']
    meeting_time = request.json['time']
    attendees = request.json['attendees']

    # Create meeting in Google Calendar
    google_api = GoogleAPI()
    event_id = google_api.create_event(meeting_title, meeting_date, meeting_time, attendees)

    # Schedule meeting in Zoom
    zoom_api = ZoomAPI()
    meeting_url = zoom_api.schedule_meeting(meeting_title, meeting_date, meeting_time, attendees)

    return {
        'event_id': event_id,
        'meeting_url': meeting_url
    }

if __name__ == '__main__':
    app.run()