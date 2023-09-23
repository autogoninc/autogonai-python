import requests
from collections import UserDict

from .error import APIError, UnauthorizedError


base_api_url = "https://api.autogon.ai/api/v1"

"""
Define a base API class that will be used to make requests to the AutoGon API.
"""
class AutoGonAPI:
    """Base class for AutoGon API."""

    @staticmethod
    def request(method: str, url: str, headers: dict, body: dict = None) -> dict:
        """Make a request to the AutoGon API.

        Args:
            method (str): HTTP method.
            url (str): URL to make request to.
            headers (dict): HTTP headers.
            body (dict, optional): HTTP body. Defaults to None.

        Raises:
            APIError: Error raised by the API.
            UnauthorizedError: Error raised when API key is invalid.

        Returns:
            dict: Response from the API.
        """

        # Construct the request URL
        url = base_api_url + url # https://api.autogon.ai/api/v1 + /projects/

        # Make request to the API if method is GET, POST, PUT, PATCH or DELETE
        if method.lower() in ["get", "post", "put", "patch", "delete"]:
            response = requests.request(method, url, headers=headers, json=body)

        # Raise an error if method is not one of the above
        else:
            raise ValueError(f"Invalid request method {method}", 400)
        
        if response.status_code == 401:
            raise UnauthorizedError()
        if response.status_code >= 400:
            raise APIError(response.json()["message"], response.status_code)
        return response
    
    @staticmethod
    def get(url: str, headers: dict) -> dict:
        """Make a GET request to the AutoGon API.

        Args:
            url (str): URL to make request to.
            headers (dict): HTTP headers.

        Returns:
            dict: Response from the API.
        """
        return AutoGonAPI.request("get", url, headers)
    
    @staticmethod
    def post(url: str, headers: dict, body: dict) -> dict:
        """Make a POST request to the AutoGon API.

        Args:
            url (str): URL to make request to.
            headers (dict): HTTP headers.
            body (dict): HTTP body.

        Returns:
            dict: Response from the API.
        """
        return AutoGonAPI.request("post", url, headers, body)
    
    @staticmethod
    def put(url: str, headers: dict, body: dict) -> dict:
        """Make a PUT request to the AutoGon API.

        Args:
            url (str): URL to make request to.
            headers (dict): HTTP headers.
            body (dict): HTTP body.

        Returns:
            dict: Response from the API.
        """
        return AutoGonAPI.request("put", url, headers, body)
    
    @staticmethod
    def patch(url: str, headers: dict, body: dict) -> dict:
        """Make a PATCH request to the AutoGon API.

        Args:
            url (str): URL to make request to.
            headers (dict): HTTP headers.
            body (dict): HTTP body.

        Returns:
            dict: Response from the API.
        """
        return AutoGonAPI.request("patch", url, headers, body)
    
    @staticmethod
    def delete(url: str, headers: dict) -> dict:
        """Make a DELETE request to the AutoGon API.

        Args:
            url (str): URL to make request to.
            headers (dict): HTTP headers.

        Returns:
            dict: Response from the API.
        """
        return AutoGonAPI.request("delete", url, headers, body=None)
    
    