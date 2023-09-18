from flask import Blueprint, request, jsonify
from .utils.google_api import GoogleAPI
from .utils.zoom_api import ZoomAPI

assistant_bp = Blueprint('assistant', __name__)

@google_bp.route('/schedule-meeting', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    # Extract necessary information from the request data
    meeting_title = data.get('title')
    meeting_date = data.get('date')
    meeting_time = data.get('time')
    attendees = data.get('attendees')

    # Create a new event in Google Calendar
    google_api = GoogleAPI()
    event_id = google_api.create_event(meeting_title, meeting_date, meeting_time, attendees)

    # Create a new meeting in Zoom
    zoom_api = ZoomAPI()
    meeting_id = zoom_api.create_meeting(meeting_title, meeting_date, meeting_time, attendees)

    # Return the event ID and meeting ID as a response
    response = {
        'event_id': event_id,
        'meeting_id': meeting_id
    }
    return jsonify(response), 200

@google_bp.route('/cancel-meeting', methods=['POST'])
def cancel_meeting():
    data = request.get_json()
    # Extract necessary information from the request data
    event_id = data.get('event_id')
    meeting_id = data.get('meeting_id')

    # Delete the event from Google Calendar
    google_api = GoogleAPI()
    google_api.delete_event(event_id)

    # Delete the meeting from Zoom
    zoom_api = ZoomAPI()
    zoom_api.delete_meeting(meeting_id)

    return jsonify({'message': 'Meeting cancelled successfully'}), 200