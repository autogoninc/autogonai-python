import json


def gen_params(arg_pairs):
    # Create an empty dictionary to store the arguments
    arguments_dict = {}

    # Get all local variables (including function arguments) as a dictionary
    local_variables = arg_pairs

    # Iterate through the local variables and store the arguments in the dictionary
    for key, value in local_variables.items():
        if key != "self":  # Exclude 'self' if it's a method within a class
            arguments_dict[key] = value

    return arguments_dict


class BaseBlock(int):
    endpoint = "engine/start"

    def __new__(cls, data):
        i = int.__new__(cls, data["block_id"])
        i.client = data["client"]
        i.project_id = data["project_id"]
        i.block_id = data["block_id"]
        i.parent_id = data["parent_id"]
        i.function_code = data["function_code"]
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
