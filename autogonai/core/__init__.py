from .api import *
from autogonai.development import Blocks
from autogonai.connector import API

from autogonai.core.project import Project


class Client(API):
    """
    The AutogonAI Python Client that acts as an interface between AutogonAI and Python projects

    Args:
        api_key (str): The API key gotten from user settings from the AutogonAI platform

    """

    def __init__(self, api_key, **kwargs):
        self.api_key = api_key

        # TODO: some functionality to validate user's api_key

        super().__init__(api_key=api_key, **kwargs)

        self.Project = Project(self)

        # self.Dashboard = Dashboard(self)
        # self.StateManagements = StateManagements(self)
        # self.Datasets = Datasets(self)
        self.Blocks = Blocks(self)
