import os
import requests


class ClientAPI:
    DEFAULT_URL = "https://flicker.appspot.com"

    def __init__(self, api_url=None):
        self.api_url = api_url if api_url is not None else DEFAULT_URL

    def post_message(self, message):
        endpoint = os.path.join(API_URL, 'message')
        body = {'message': message}
        r = requests.post(url=endpoint, data=body)

    def get_messages(self):
        endpoint = os.path.join(API_URL, 'messages')

        response = requests.get(url=endpoint)
        return response.json()
