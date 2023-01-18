class Blocks:
    import autogonai.development.data_processing as dp
    # from autogonai.development import DataInput
    
    endpoint = "engine/start"
    
    # DataInput = 'DP_1'

    def __init__(self, client):
        self.client = client

    def get(self):
        pass
    
    # def new(self,
    #     client,
    #     function_code: str,
    #     project_id: int,
    #     block_id: int,
    #     parent_id: int = 0,):
        
    #     data = {
    #         "client": client,
    #         "project_id": project_id,
    #         "parent_id": parent_id,
    #         "block_id": block_id,
    #         "function_code": function_code,
    #     }
        
    #     if function_code == self.DataInput: return dp.DataInput(data)

    def DataInput(self): return dp.DataInput(self.client)


class BaseBlock:
    def __init__(
        self,
        client,
        function_code: str,
        project_id: int,
        block_id: int,
        parent_id: int = 0,
    ) -> None:
        self.client = client
        self.body = {
            "project_id": project_id,
            "parent_id": parent_id,
            "block_id": block_id,
            "function_code": function_code,
            "args": {},
            "flowjson": [],
        }
        self.params = {}

    def set_params(self, **kwargs):
        self.params = kwargs
        return self.params

    def run(self):
        self.body["args"] = self.params
        return self.client.send_request(Blocks.endpoint, self.body)
