import json
import requests
from .erros import AutogonRequestError, AutogonServerError

test_header = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNjYzODU1LCJqdGkiOiIyNDUzZWE1YTU1ZWY0YTZhYTRmZTRjMDAzMzQ2NDk0MiIsInVzZXJfaWQiOjZ9.4qgVMwvkxYZgN5CzLrMEk-0SWq4Rtoq2zh17i2QDdrA"}

class API:
    def __init__(
        self,
        api_key=None,
        base_url=None,
        timeout=None,
        show_header=False,
        show_request=True,
        proxies=None,
    ):
        if not base_url:
            # self.url = "https://autogon.ai/api/v1/"
            self.url = "http://127.0.0.1:8000/api/v1/"
        else:
            self.url = base_url
        self.api_key = api_key

    def send_request(self, endpoint, payload={}, method='post'):
        url = self.url + endpoint

        # response = requests.post(url, headers={"X-AUG-KEY": self.api_key}, json=payload)
        if method.lower() == 'post':
            response = requests.post(url, headers=test_header, json=payload)
        elif method.lower() == 'get':
            response = requests.get(url, headers=test_header)
        elif method.lower() == 'delete':
            response = requests.delete(url, headers=test_header)

        self._handle_exceptions(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        
        if type(data) == str:
            # print(data)
            raise AutogonServerError('data')

        if data.get('status') == 'false':
            raise AutogonRequestError(data['message'])

        return data

    def _handle_exceptions(self, response):
        pass
