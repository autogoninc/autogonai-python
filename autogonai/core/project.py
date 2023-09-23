# This will be the main file for the project class

from .api import AutoGonAPI

class Project(AutoGonAPI):
    """
    Handles all project related operations.
    """

    endpoint = "/engine/project/"

    # I dont understand how this works
    # def __init__(self, client):
    #     self.client = client

    @classmethod
    def get_project(cls, app_id: str) -> dict:
        """Fetches an existing project.

        Args:
            app_id (str): Project UUID.

        Returns:
            dict: Project details.
        """
        response = cls.request("get", cls.endpoint + app_id + "/")
        return response
    
    @classmethod
    def create_project(cls, name: str, description: str) -> dict:
        """Create a project.

        Args:
            name (str): Name of the project.
            description (str): Short description for project.

        Returns:
            dict: Project details.
        """
        body = {"project_name": name, "project_description": description}
        response = cls.request("post", cls.endpoint, body)
        return response
    
    @classmethod
    def delete_project(cls, app_id: str) -> str:
        """Deletes a project.

        Args:
            app_id (str): Project UUID.

        Returns:
            str: Confirmation of delete.
        """
        response = cls.request("delete", cls.endpoint + app_id + "/")
        return response
    

# How to use the Project class
# from autogonai.core import Project

# project = Project.create_project("Project #0", "This is a short description for my first project")
