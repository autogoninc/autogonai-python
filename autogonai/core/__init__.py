from .api import *
from development import Blocks
from autogonai.connector import API


class Client(API):

    def __init__(self, api_key, **kwargs):
        self.api_key = api_key

        # TODO: some functionality to validate user's api_key

        super().__init__(api_key=api_key, **kwargs)

        self.Dashboard = Dashboard(self)
        self.Project = Project(self)
        self.StateManagement = StateManagement(self)
        self.Dataset = Dataset(self)
        self.Blocks = Blocks(self)

