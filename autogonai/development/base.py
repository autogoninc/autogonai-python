import json


class BaseBlock:

    endpoint = "engine/start"

    def __init__(self, data) -> None:
        self.client = data["client"]
        self.body = {
            "project_id": int(data["project_id"]),
            "parent_id": int(data["parent_id"]),
            "block_id": int(data["block_id"]),
            "function_code": str(data["function_code"]),
            "args": {},
            "flowjson": [],
        }
        self.params = {}

    def set_params(self, **kwargs):
        self.params = kwargs
        return self.params

    def run(self):
        self.body["args"] = self.params
        response = self.client.send_request(self.endpoint, self.body)
        return response
