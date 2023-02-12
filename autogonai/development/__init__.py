class Blocks:
    import autogonai.development.data_processing as dp
    import autogonai.development.machine_learning as ml
    import autogonai.development.deep_learning as dl
    
    
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
        
        elif function_code == self.fc.ArtificialNeuralNetworkInit:
            return self.dl.ArtificialNeuralNetworkInit(data)
        elif function_code == self.fc.ArtificialNeuralNetworkTrain:
            return self.dl.ArtificialNeuralNetworkTrain(data)
        elif function_code == self.fc.ArtificialNeuralNetworkEvaluate:
            return self.dl.ArtificialNeuralNetworkEvaluate(data)
        elif function_code == self.fc.ArtificialNeuralNetworkPredict:
            return self.dl.ArtificialNeuralNetworkPredict(data)
        elif function_code == self.fc.SelfOrganizingMapsInit:
            return self.dl.SelfOrganizingMapsInit(data)
        elif function_code == self.fc.SelfOrganizingMapsTrain:
            return self.dl.SelfOrganizingMapsTrain(data)
        elif function_code == self.fc.SelfOrganizingMapsPredict:
            return self.dl.SelfOrganizingMapsPredict(data)
        elif function_code == self.fc.RestrictedBoltzmannMachineInit:
            return self.dl.RestrictedBoltzmannMachineInit(data)
        elif function_code == self.fc.RestrictedBoltzmannMachineTrain:
            return self.dl.RestrictedBoltzmannMachineTrain(data)
        elif function_code == self.fc.RestrictedBoltzmannMachineTransform:
            return self.dl.RestrictedBoltzmannMachineTransform(data)
        
        
    # def InputData(self): return dp.InputData(self.client)
