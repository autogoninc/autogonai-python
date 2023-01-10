class Dashboard:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass


class Project:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create(self, name: str, description: str) -> dict:
        """Create a project

        Args:
            name (str): name of the project
            description (str): short description for project

        Returns:
            dict: Project details
        """
        # make a request to autogon creating a project
        # ...with the above parameters
        pass

    def delete(self):
        pass


class StateManagement:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass


class Dataset:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def create():
        pass

    def delete(self):
        pass


class FunctionCode:
    def __init__(self, client):
        self.client = client

    def get(self):
        pass
