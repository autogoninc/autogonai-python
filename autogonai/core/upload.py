# This file contains the Upload class, which is used to upload datasets to AutoGonAI.

from .api import AutoGonAPI

class Upload(AutoGonAPI):
    """
    Handles all dataset/file upload related operations.
    """

    endpoint = "/engine/upload/"

    # def __init__(self, client):
    #     self.client = client

    @classmethod
    def upload_file(cls, file_path: str) -> dict:
        """Uploads a file to AutoGonAI.

        Args:
            file_path (str): Path to file to be uploaded.

        Returns:
            dict: File details.
        """
        with open(file_path, "rb") as f:
            response = cls.request("post", cls.endpoint, {"file": f})
        return response