class Blocks:
    import autogonai.development.data_processing as dp
    from autogonai.constants import function_codes as fc

    endpoint = "engine/start"

    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def new( # Slower structure to implemnt
        self,
        function_code: str,
        project_id: int,
        block_id: int,
        parent_id: int = 0,
    ):

        data = {
            "client": self.client,
            "project_id": project_id,
            "parent_id": parent_id,
            "block_id": block_id,
            "function_code": function_code,
        }

        if function_code == self.fc.InputData:
            return self.dp.InputData(data)
        elif function_code == self.fc.HandleMissingData:
            return self.dp.HandleMissingData(data)
        elif function_code == self.fc.EncodeData:
            return self.dp.EncodeData(data)
        elif function_code == self.fc.SplitData:
            return self.dp.SplitData(data)
        elif function_code == self.fc.FeatureScaleData:
            return self.dp.FeatureScaleData(data)
        elif function_code == self.fc.DropColumns:
            return self.dp.DropColumns(data)
        elif function_code == self.fc.TimeStepData:
            return self.dp.TimeStepData(data)

    # def InputData(self): return dp.InputData(self.client)
