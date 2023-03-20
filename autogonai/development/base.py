import json


class BaseBlock(int):

    endpoint = "engine/start"

    def __new__(cls, data):
        i = int.__new__(cls, data['block_id'])
        i.client = data["client"]
        i.project_id = data['project_id']
        i.block_id = data['block_id']
        i.parent_id = data['parent_id']
        i.function_code = data['function_code']
        i.params = {}
        return i

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
