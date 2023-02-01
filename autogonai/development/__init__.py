class Blocks:
    import autogonai.development.data_processing as dp
    import autogonai.development.machine_learning as ml
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
        
        elif function_code == self.fc.SimpleLinearRegression:
            return self.ml.SimpleLinearRegression(data)
        elif function_code == self.fc.SimpleLinearRegressionPredict:
            return self.ml.SimpleLinearRegressionPredict(data)
        elif function_code == self.fc.MultipleLinearRegression:
            return self.ml.SimpleLinearRegression(data)
        elif function_code == self.fc.MultipleLinearRegressionPredict:
            return self.ml.MultipleLinearRegressionPredict(data)
        elif function_code == self.fc.PolynomialLinearRegression:
            return self.ml.PolynomialLinearRegression(data)
        elif function_code == self.fc.PolynomialLinearRegressionPredict:
            return self.ml.PolynomialLinearRegressionPredict(data)
        elif function_code == self.fc.SupportVectorRegression:
            return self.ml.SupportVectorRegression(data)
        elif function_code == self.fc.SupportVectorRegressionPredict:
            return self.ml.SupportVectorRegressionPredict(data)
        elif function_code == self.fc.DecisionTreeRegression:
            return self.ml.DecisionTreeRegression(data)
        elif function_code == self.fc.DecisionTreeRegressionPredict:
            return self.ml.DecisionTreeRegressionPredict(data)
        elif function_code == self.fc.RandomForestRegression:
            return self.ml.RandomForestRegression(data)
        elif function_code == self.fc.RandomForestRegressionPredict:
            return self.ml.RandomForestRegressionPredict(data)
        
        
    # def InputData(self): return dp.InputData(self.client)
