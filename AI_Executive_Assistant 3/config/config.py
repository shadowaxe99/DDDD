config.py:


import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    ZOOM_CLIENT_ID = os.environ.get('ZOOM_CLIENT_ID')
    ZOOM_CLIENT_SECRET = os.environ.get('ZOOM_CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI') or 'http://localhost:5000/callback'
    SCOPE = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.readonly']
    ZOOM_API_BASE_URL = 'https://api.zoom.us/v2'
    ZOOM_API_TOKEN_URL = 'https://zoom.us/oauth/token'
    ZOOM_API_MEETINGS_URL = 'https://api.zoom.us/v2/users/me/meetings'

