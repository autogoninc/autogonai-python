import json


class BaseBlock:

    endpoint = "engine/start"

    def __init__(self, data) -> None:
        self.client = data["client"]
        self.project_id = data['project_id']
        self.block_id = data['block_id']
        self.parent_id = data['parent_id']
        self.function_code = data['function_code']
        self.params = {}

    def set_params(self, **kwargs):
        self.params = kwargs
        return self.params

    def run(self):
        body = {
            "project_id": self.project_id,
            "parent_id": self.parent_id,
            "block_id": self.block_id,
            "function_code": self.function_code,
            "args": self.params,
        }
        response = self.client.send_request(self.endpoint, body)
        return response
