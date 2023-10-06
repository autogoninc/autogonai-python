from .qore import *


class Projects:
    """Handles operations related to projects."""

    endpoint = "engine/project/"

    def __init__(self, client: any):
        """Initializes the Projects class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def get(self, app_id) -> dict:
        """Fetches an existing Project by its UUID.

        Args:
            app_id (str): UUID of the project.

        Returns:
            dict: Project details.
        """
        response = self.client.send_request(self.endpoint + app_id, method="get")
        return response

    def create(self, name: str, description: str) -> dict:
        """Creates a new project.

        Args:
            name (str): Name of the project.
            description (str): Short description for the project.

        Returns:
            dict: Project details.
        """
        body = {"project_name": name, "project_description": description}
        response = self.client.send_request(self.endpoint, body)
        return response

    def delete(self, app_id) -> str:
        """Deletes a project by its UUID.

        Args:
            app_id (str): UUID of the project.

        Returns:
            str: Confirmation of the deletion.
        """
        response = self.client.send_request(self.endpoint + app_id, method="delete")
        return response


# class Project(int):
#     """Represents a project with additional metadata."""

#     data = {}
#     id = 0
#     app_id = ""
#     name = ""
#     description = ""
#     compiled_models = {}

#     def __new__(cls, data: dict):
#         """Creates a new Project instance.

#         Args:
#             data (dict): Project data.

#         Returns:
#             Project: Project instance.
#         """
#         i = int.__new__(cls, data["id"])
#         i.data = data
#         i.id = data["id"]
#         i.app_id = data["app_id"]
#         i.name = data["project_name"]
#         i.description = data["project_description"]
#         i.compiled_models = data["project_compiled_models"]
#         return i


class StateManagements:
    """Handles operations related to state management."""

    endpoint = "engine/statemanagement/"

    def __init__(self, client: any):
        """Initializes the StateManagements class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def get(self, id) -> dict:
        """Fetches state management details by ID.

        Args:
            id (int): ID of the state management.

        Returns:
            dict: State management details.
        """
        response = self.client.send_request(self.endpoint + str(id), method="get")
        return response

    def list(self) -> dict:
        """Lists all available state managements.

        Returns:
            dict: List of state managements.
        """
        response = self.client.send_request(self.endpoint, method="get")
        return response

    def delete(self, id) -> dict:
        """Deletes a state management by ID.

        Args:
            id (int): ID of the state management.

        Returns:
            dict: Confirmation of the deletion.
        """
        response = self.client.send_request(self.endpoint + str(id), method="delete")
        return response


class Datasets:
    """Handles operations related to datasets."""

    endpoint = "engine/dataset/"

    def __init__(self, client: any):
        """Initializes the Datasets class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def get(self, id) -> dict:
        """Fetches dataset details by ID.

        Args:
            id (int): ID of the dataset.

        Returns:
            dict: Dataset details.
        """
        response = self.client.send_request(self.endpoint + str(id), method="get")
        return response

    def list(self) -> dict:
        """Lists all available datasets.

        Returns:
            dict: List of datasets.
        """
        response = self.client.send_request(self.endpoint, method="get")
        return response

    def create(self, name: str, description: str, dataset_url: str) -> dict:
        """Creates a new dataset.

        Args:
            name (str): Name of the dataset.
            description (str): Description of the dataset.
            dataset_url (str): URL of the dataset.

        Returns:
            dict: Dataset details.
        """
        body = {"name": name, "description": description, "dataset_url": dataset_url}
        response = self.client.send_request(
            self.endpoint, json_data=body, method="post"
        )
        return response

    def update(self, id, name: str, description: str) -> dict:
        """Updates an existing dataset.

        Args:
            id (int): ID of the dataset to update.
            name (str): New name for the dataset.
            description (str): New description for the dataset.

        Returns:
            dict: Dataset details after the update.
        """
        body = {"dataset_name": name, "description": description}
        response = self.client.send_request(
            self.endpoint + str(id), json_data=body, method="post"
        )
        return response

    def delete(self, id) -> dict:
        """Deletes a dataset by ID.

        Args:
            id (int): ID of the dataset to delete.

        Returns:
            dict: Confirmation of the deletion.
        """
        response = self.client.send_request(self.endpoint + str(id), method="delete")
        return response


class Production:
    """Handles operations related to production pipelines."""

    endpoint = "models/"

    def __init__(self, client: any):
        """Initializes the Production class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def generate_dataset(self, data: dict) -> dict:
        """Generates a dataset based on the provided data.

        Args:
            data (dict): Data to generate the dataset.

        Returns:
            dict: Generated dataset details.
        """
        body = {"data": data}
        response = self.client.send_request(
            self.endpoint + "generate/", json_data=body, method="post"
        )
        return response

    def run_pipeline(self, flow_id, data: dict) -> dict:
        """Runs a production pipeline with the given flow ID and test data.

        Args:
            flow_id: ID of the flow to run.
            data (dict): Test data for the pipeline.

        Returns:
            dict: Results of the production pipeline run.
        """
        body = {"flow_id": flow_id, "data": data}
        response = self.client.send_request(
            self.endpoint + "production/", json_data=body, method="post"
        )
        return response


class Qore:
    def __init__(self, client: any):
        """Initializes the Production class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

        self.VisionAI = Vision(client)
        self.NaturalLanguageAI = NaturalLanguage(client)
        self.Voice = Voice(client)
