import unittest
from app.main import schedule_zoom_meeting

class TestMain(unittest.TestCase):
    def test_schedule_zoom_meeting(self):
        # Test case 1: Successful scheduling of Zoom meeting
        meeting_id = schedule_zoom_meeting("John Doe", "john.doe@example.com", "2021-12-01 10:00", "2021-12-01 11:00")
        self.assertIsNotNone(meeting_id)

        # Test case 2: Invalid email address
        with self.assertRaises(ValueError):
            schedule_zoom_meeting("Jane Doe", "jane.doe", "2021-12-01 10:00", "2021-12-01 11:00")

        # Test case 3: Invalid meeting time
        with self.assertRaises(ValueError):
            schedule_zoom_meeting("Jane Doe", "jane.doe@example.com", "2021-12-01 11:00", "2021-12-01 10:00")

if __name__ == '__main__':
    unittest.main()