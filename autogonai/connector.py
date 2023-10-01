# Import necessary libraries
import json
import requests
from .errors import AutogonRequestError, AutogonServerError


class API:
    def __init__(
        self,
        api_key,
        base_url=None,
        timeout=None,
        show_header=False,
        show_request=True,
        proxies=None,
    ):
        """
        Initialize the API class.

        Args:
            api_key (str): API key for authentication. Defaults to None.
            base_url (str, optional): Base URL for API requests. Defaults to None.
            timeout (int, optional): Timeout for API requests in seconds. Defaults to None.
            show_header (bool, optional): Flag to show request header. Defaults to False.
            show_request (bool, optional): Flag to show request details. Defaults to True.
            proxies (dict, optional): Proxy settings for API requests. Defaults to None.
        """
        # Initialize class attributes
        if not base_url:
            self.url = "https://api.autogon.ai/api/v1/"
        else:
            self.url = base_url
        self.api_key = api_key
        self.header = {"X-AUG-KEY": api_key}

    # Define a method to send HTTP requests
    def send_request(self, endpoint, json_data=None, form_data=None, method="post"):
        """
        Send an HTTP request to the specified endpoint.

        Args:
            endpoint (str): API endpoint to send the request to.
            payload (dict, optional): Data to be sent with the request. Defaults to {}.
            method (str, optional): HTTP method for the request (post, get, patch, put, delete). Defaults to "post".

        Returns:
            dict: JSON response from the API.
        """
        url = self.url + endpoint

        # Send an HTTP request based on the specified method
        if method.lower() == "post":
            response = requests.post(
                url, headers=self.header, json=json_data, data=form_data
            )
        elif method.lower() == "get":
            response = requests.get(url, headers=self.header)
        elif method.lower() == "patch":
            response = requests.patch(
                url, headers=self.header, json=json_data, data=form_data
            )
        elif method.lower() == "put":
            response = requests.put(
                url, headers=self.header, json=json_data, data=form_data
            )
        elif method.lower() == "delete":
            response = requests.delete(url, headers=self.header)

        # Handle exceptions that may occur during the request

        try:
            data = response.json()
        except ValueError:
            data = response.text

        if type(data) == str:
            # print(data)
            raise AutogonServerError(response.status_code, data)

        if data.get("status") == "false":
            raise AutogonRequestError(response.status_code, data["message"])

        # Check the response data for errors and raise exceptions if necessary
        if type(data) == str:
            raise AutogonServerError(response.status_code, data)

        if data.get("status") in ["false", False]:
            raise AutogonRequestError(response.status_code, data["message"])

        return data
