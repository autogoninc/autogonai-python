class Blocks:
    import autogonai.development.data_processing as dp
    from autogonai.constants import function_codes as fc
    # from autogonai.development import DataInput
    
    endpoint = "engine/start"

    def __init__(self, client):
        self.client = client

    def get(self):
        pass
    
    def new(self,
        function_code: str,
        project_id: int,
        block_id: int,
        parent_id: int = 0,):
        
        data = {
            "client": self.client,
            "project_id": project_id,
            "parent_id": parent_id,
            "block_id": block_id,
            "function_code": function_code,
        }
        
        if function_code == self.fc.DataInput: return self.dp.DataInput(data)
        if function_code == self.fc.DropColumns: return self.dp.DropColumns(data)

    # def DataInput(self): return dp.DataInput(self.client)

