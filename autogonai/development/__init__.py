class Blocks:
    import autogonai.development.data_processing as dp
    import autogonai.development.machine_learning as ml
    import autogonai.development.auto_machine_learning as aml
    import autogonai.development.deep_learning as dl
    import autogonai.development.auto_deep_learning as adl

    from autogonai.constants import function_codes as fc
    from autogonai.development.base import BaseBlock

    endpoint = "engine/start"

    def __init__(self, client):
        self.client = client

    def get(self):
        pass

    def new(  # Slower structure to implemnt
        self,
        function_code: str,
        project_id: int,
        id: int,
        parent: int = 0,
    ) -> BaseBlock:
        data = {
            "client": self.client,
            "project_id": project_id,
            "parent_id": parent,
            "block_id": id,
            "function_code": function_code,
        }

        functions = vars(self.fc)

        # Main functions finder
        if function_code in functions.values():
            function_name = [k for k, v in functions.items() if v == function_code][0]
            if function_code.startswith("DP"):
                func = getattr(self.dp, function_name)
                return func(data)
            elif function_code.startswith("ML"):
                func = getattr(self.ml, function_name)
                return func(data)
            elif function_code.startswith("DL"):
                func = getattr(self.dl, function_name)
                return func(data)
            elif function_code.startswith("AUTO"):
                func = getattr(self.aml, function_name)
                return func(data)
            elif function_code.startswith("A_DL"):
                func = getattr(self.adl, function_name)
                return func(data)

        # Keeping this for user developement purposes
        elif function_code == self.fc.DataInput:
            return self.dp.DataInput(data)
        elif function_code == self.fc.HandleMissingData:
            return self.dp.HandleMissingData(data)
        elif function_code == self.fc.DataEncoding:
            return self.dp.DataEncoding(data)
        elif function_code == self.fc.DataSplitting:
            return self.dp.DataSplitting(data)
        elif function_code == self.fc.FeatureScaleData:
            return self.dp.FeatureScaling(data)
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
        elif function_code == self.fc.LogisticRegression:
            return self.ml.LogisticRegression(data)
        elif function_code == self.fc.LogisticRegressionPredict:
            return self.ml.LogisticRegressionPredict(data)
        elif function_code == self.fc.KNearestNeighbors:
            return self.ml.KNearestNeighbors(data)
        elif function_code == self.fc.KNearestNeighborsPredict:
            return self.ml.KNearestNeighborsPredict(data)
        elif function_code == self.fc.SupportVectorMachine:
            return self.ml.SupportVectorMachine(data)
        elif function_code == self.fc.SupportVectorMachinePredict:
            return self.ml.SupportVectorMachinePredict(data)
        elif function_code == self.fc.KernelSupportVectorMachine:
            return self.ml.KernelSupportVectorMachine(data)
        elif function_code == self.fc.KernelSupportVectorMachinePredict:
            return self.ml.KernelSupportVectorMachinePredict(data)
        elif function_code == self.fc.NaiveBayes:
            return self.ml.NaiveBayes(data)
        elif function_code == self.fc.NaiveBayesPredict:
            return self.ml.NaiveBayesPredict(data)
        elif function_code == self.fc.DecisionTreeClassification:
            return self.ml.DecisionTreeClassification(data)
        elif function_code == self.fc.DecisionTreeClassificationPredict:
            return self.ml.DecisionTreeClassificationPredict(data)
        elif function_code == self.fc.RandomForestClassification:
            return self.ml.RandomForestClassification(data)
        elif function_code == self.fc.RandomForestClassificationPredict:
            return self.ml.RandomForestClassificationPredict(data)
        elif function_code == self.fc.HierarchicalClustering:
            return self.ml.HierarchicalClustering(data)
        elif function_code == self.fc.HierarchicalClusteringPredict:
            return self.ml.HierarchicalClusteringPredict(data)
        elif function_code == self.fc.KMeansClustering:
            return self.ml.KMeansClustering(data)
        elif function_code == self.fc.KMeansClusteringPredict:
            return self.ml.KMeansClusteringPredict(data)
        elif function_code == self.fc.XGBoost:
            return self.ml.XGBoost(data)
        elif function_code == self.fc.XGBoostPredict:
            return self.ml.XGBoostPredict(data)

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
