import json
import requests


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
            self.url = "https://autogon.ai/api/v1/"
        else:
            self.url = base_url

    def send_request(self, endpoint, payload):
        url = self.url + endpoint

        response = requests.post(url, headers={"X-AUG-KEY": self.api_key}, json=payload)

        self._handle_exceptions(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text

        return data

    def _handle_exceptions(self, response):
        pass
