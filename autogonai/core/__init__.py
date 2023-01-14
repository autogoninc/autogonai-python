from .api import *
from autogonai.connector import API


class Client(API):

    from autogonai.development.data_processing import (
        data_input,
        missing_data,
        feature_scaling,
        data_encode,
    )

    def __init__(self, api_key, **kwargs):
        self.api_key = api_key

        # TODO: some functionality to validate user's api_key 

        super().__init__(api_key=api_key, **kwargs)

        self.Dashboard = Dashboard(self)
        self.Project = Project(self)
        self.StateManagement = StateManagement(self)
        self.Dataset = Dataset(self)
        self.FunctionCode = FunctionCode(self)
