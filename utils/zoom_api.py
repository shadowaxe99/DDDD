import requests
import json

class ZoomAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.zoom.us/v2"

    def create_meeting(self, topic, start_time, duration, password):
        url = f"{self.base_url}/users/me/meetings"
        headers = {
            "Authorization": f"Bearer {self._get_access_token()}",
            "Content-Type": "application/json"
        }
        data = {
            "topic": topic,
            "type": 2,
            "start_time": start_time,
            "duration": duration,
            "password": password
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def _get_access_token(self):
        url = "https://zoom.us/oauth/token"
        headers = {
            "Authorization": f"Basic {self._get_encoded_credentials()}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }
        response = requests.post(url, headers=headers, data=data)
        return response.json()["access_token"]

    def _get_encoded_credentials(self):
        credentials = f"{self.api_key}:{self.api_secret}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        return encoded_credentials