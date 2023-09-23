# This will be the main file for the dataset class

from .api import AutoGonAPI

class Dataset(AutoGonAPI):
    """
    Handles all dataset related operations.
    """

    endpoint = "/engine/datasets/"

    # I dont understand how this works
    # def __init__(self, client):
    #     self.client = client

    @classmethod
    def get_dataset(cls, dataset_id: int) -> dict:
        """Fetches an existing dataset.

        Args:
            dataset_id (str): Dataset ID.

        Returns:
            dict: Dataset details.
        """
        response = cls.request("get", cls.endpoint + dataset_id + "/")
        return response
    
    @classmethod
    def get_datasets(cls) -> dict:
        """Fetches all existing datasets.

        Returns:
            dict: Dataset List (Unpaginated).
        """
        response = cls.request("get", cls.endpoint + "list/") # list/
        return response
    
    @classmethod
    def create_dataset(cls, name: str, description: str, type: str, url: str) -> dict:
        """Create a dataset.

        Args:
            name (str): Name of the dataset.
            description (str): Short description for dataset.
            type (str): Type of dataset (csv, json, etc).
            url (str): URL of dataset.

        Returns:
            dict: Dataset details.
        """
        body = {
            "dataset_name": name, 
            "dataset_description": description, 
            "dataset_type": type, 
            "dataset_url": url
            }
        response = cls.request("post", cls.endpoint, body)
        return response
    
    @classmethod
    def delete_dataset(cls, dataset_id: int) -> str:
        """Deletes a dataset.

        Args:
            dataset_id (str): Dataset ID.

        Returns:
            str: Confirmation of delete.
        """
        response = cls.request("delete", cls.endpoint + dataset_id + "/")
        return response