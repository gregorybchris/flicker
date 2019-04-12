import os
import requests


class ClientAPI:
    DEFAULT_URL = "https://flicker.appspot.com"

    def __init__(self, api_url=None):
        self._api_url = api_url if api_url is not None else ClientAPI.DEFAULT_URL

    def post_message(self, message):
        endpoint = os.path.join(self._api_url, 'message')
        body = {'message': message}
        r = requests.post(url=endpoint, data=body)

    def get_messages(self):
        endpoint = os.path.join(self._api_url, 'messages')

        response = requests.get(url=endpoint)
        return response.json()
