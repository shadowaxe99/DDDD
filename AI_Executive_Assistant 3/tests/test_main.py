import unittest
from app.main import *

class TestAIExecutiveAssistant(unittest.TestCase):
    def test_schedule_zoom_meeting(self):
        # Test case for scheduling a Zoom meeting
        meeting_id = schedule_zoom_meeting("Meeting Title", "2022-01-01", "10:00 AM", "11:00 AM")
        self.assertIsNotNone(meeting_id)

    def test_get_upcoming_meetings(self):
        # Test case for getting upcoming meetings
        meetings = get_upcoming_meetings()
        self.assertIsInstance(meetings, list)

    def test_send_zoom_invitation(self):
        # Test case for sending a Zoom invitation
        invitation_sent = send_zoom_invitation("meeting@example.com", "Meeting Title", "2022-01-01", "10:00 AM", "11:00 AM")
        self.assertTrue(invitation_sent)

if __name__ == '__main__':
    unittest.main()