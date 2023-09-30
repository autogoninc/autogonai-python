# Import necessary libraries
import json
import requests
from .errors import AutogonRequestError, AutogonServerError

# Define a test header with an authorization token
test_header = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2NTAyNzYzLCJqdGkiOiIwZTI4NDI4YWVhY2U0Mzg3YjRlMDY3ZjRkZDQ1MDU5YyIsInVzZXJfaWQiOjl9.mWhfLm8ptiYngvTpKYnp4ytQU08HqBh3Vux7_9gXZvc"
}


# Define a class named 'API'
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
        # Initialize class attributes
        if not base_url:
            self.url = "https://api.autogon.ai/api/v1/"
        else:
            self.url = base_url
        self.api_key = api_key

    # Define a method to send HTTP requests
    def send_request(self, endpoint, payload={}, method="post"):
        url = self.url + endpoint

        # Send an HTTP request based on the specified method
        if method.lower() == "post":
            response = requests.post(url, headers=test_header, json=payload)
        elif method.lower() == "get":
            response = requests.get(url, headers=test_header)
        elif method.lower() == "patch":
            response = requests.patch(url, headers=test_header)
        elif method.lower() == "put":
            response = requests.put(url, headers=test_header, json=payload)
        elif method.lower() == "delete":
            response = requests.delete(url, headers=test_header)

        # Handle exceptions that may occur during the request
        self._handle_exceptions(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text

        # Check the response data for errors and raise exceptions if necessary
        if type(data) == str:
            raise AutogonServerError(response.status_code, data)

        if data.get("status") == "false":
            raise AutogonRequestError(response.status_code, data["message"])

        return data

    # Define a private method to handle exceptions (currently empty)
    def _handle_exceptions(self, response):
        pass
