from flask import Blueprint, request, jsonify
from .models import Meeting
from .utils import create_zoom_meeting, send_email

views_bp = Blueprint('views', __name__)

@views_bp.route('/schedule-meeting', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    meeting = Meeting(data['title'], data['start_time'], data['end_time'], data['attendees'])
    
    # Create Zoom meeting
    zoom_meeting_id = create_zoom_meeting(meeting)
    
    # Send email with Zoom meeting details
    send_email(meeting, zoom_meeting_id)
    
    return jsonify({'message': 'Meeting scheduled successfully'})

@views_bp.route('/cancel-meeting', methods=['POST'])
def cancel_meeting():
    data = request.get_json()
    meeting_id = data['meeting_id']
    
    # Cancel Zoom meeting
    cancel_zoom_meeting(meeting_id)
    
    return jsonify({'message': 'Meeting cancelled successfully'})