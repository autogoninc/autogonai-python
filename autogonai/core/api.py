import requests
from collections import UserDict


# Define a class named 'Dashboard'
class Dashboard:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass


# Define a class named 'Projects' for project-specific operations
class Projects:
    """Handles all Project Specific operations"""

    endpoint = "engine/project/"

    def __init__(self, client):
        self.client = client

    def get(self, app_id: str):
        """Fetches an existing Project

        Args:
            app_id (str): Project UUID

        Returns:
            dict: Project details
        """
        response = self.client.send_request(self.endpoint + app_id, method="get")
        print(response)
        return Project(response)

    def create(self, name: str, description: str) -> dict:
        """Create a project

        Args:
            name (str): name of the project
            description (str): short description for project

        Returns:
            dict: Project details
        """
        body = {"project_name": name, "project_description": description}
        response = self.client.send_request(self.endpoint, body)
        return response

    def delete(self, app_id: str) -> str:
        """Deletes a project

        Args:
            app_id (str): Project UUID

        Returns:
            str: Confirmation of delete
        """
        response = self.client.send_request(self.endpoint + app_id, method="delete")
        return response


# Define a class named 'Project' that inherits from 'int'
class Project(int):
    data = {}
    id = 0
    app_id = ""
    name = ""
    description = ""
    compiled_models = {}

    def __new__(cls, data):
        i = int.__new__(cls, data["id"])
        i.data = data
        i.id = data["id"]
        i.app_id = data["app_id"]
        i.name = data["project_name"]
        i.description = data["project_description"]
        i.compiled_models = data["project_compiled_models"]
        return i


# Define a class named 'StateManagements' for state management operations
class StateManagements:
    """Handles all StateManagement Specific operations"""

    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass


# Define a class named 'Datasets' for dataset operations
class Datasets:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass
