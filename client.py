import json
import os
import requests


class Client:
    DEFAULT_URL = "https://flicker.appspot.com"
    DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, api_url=None, extra_headers=None):
        self._api_url = api_url if api_url is not None else Client.DEFAULT_URL
        self._headers = Client.DEFAULT_HEADERS
        if extra_headers is not None:
            for k, v in extra_headers.items():
                self._headers[k] = v

    def _post(self, endpoint, content):
        endpoint = os.path.join(self._api_url, endpoint)
        body = json.dumps(content)
        return requests.post(url=endpoint, headers=self._headers, data=body)

    def _get(self, endpoint, params=None):
        endpoint = os.path.join(self._api_url, endpoint)
        # TODO: Format and pass GET params
        return requests.get(url=endpoint)

    def post_message(self, message):
        return self._post('message', {'message': message})

    def get_messages(self):
        return self._get('messages')

    def post_ultrasonic(self, reading):
        return self._post('sonic', {'reading': reading})

    def get_ultrasonics(self):
        return self._get('sonics')
