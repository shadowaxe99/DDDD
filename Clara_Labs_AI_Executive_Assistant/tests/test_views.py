import unittest
from django.test import TestCase
from app.views import *

class TestViews(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_task_view(self):
        response = self.client.get('/task/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task.html')

    def test_calendar_view(self):
        response = self.client.get('/calendar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar.html')

    def test_email_view(self):
        response = self.client.get('/email/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'email.html')

if __name__ == '__main__':
    unittest.main()