import json
import os
import requests


class ClientAPI:
    DEFAULT_URL = "https://flicker.appspot.com"
    DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, api_url=None, extra_headers=None):
        self._api_url = api_url if api_url is not None else ClientAPI.DEFAULT_URL
        self._headers = ClientAPI.DEFAULT_HEADERS
        if extra_headers is not None:
            for k, v in extra_headers.items():
                self._headers[k] = v

    def post_message(self, message):
        endpoint = os.path.join(self._api_url, 'message')
        body = json.dumps({'message': message})
        return requests.post(url=endpoint, headers=self._headers, data=body)

    def get_messages(self):
        endpoint = os.path.join(self._api_url, 'messages')
        return requests.get(url=endpoint)
