from autogonai.development.base import BaseBlock


class SimpleLinearRegression(BaseBlock):
    def set_params(self, model_name: str):
        """SimpleLinearRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class SimpleLinearRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """SimpleLinearRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class MultipleLinearRegression(BaseBlock):
    def set_params(self, model_name: str):
        """MultipleLinearRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class MultipleLinearRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """MultipleLinearRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class PolynomialLinearRegression(BaseBlock):
    def set_params(self, model_name: str, degree: int = 2):
        """PolynomialLinearRegression Parameters"""
        self.params = {"model_name": model_name, "degree": degree}
        return self.params


class PolynomialLinearRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """PolynomialLinearRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class SupportVectorRegression(BaseBlock):
    def set_params(self, model_name: str, kernel: str = "rbf"):
        """SupportVectorRegression Parameters"""
        self.params = {"model_name": model_name, "kernel": kernel}
        return self.params


class SupportVectorRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """SupportVectorRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class DecisionTreeRegression(BaseBlock):
    def set_params(self, model_name: str, random_state: int = 0):
        """DecisionTreeRegression Parameters"""
        self.params = {"model_name": model_name, "random_state": random_state}
        return self.params


class DecisionTreeRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """DecisionTreeRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class RandomForestRegression(BaseBlock):
    def set_params(
        self, model_name: str, n_estimators: int = 100, random_state: int = 0
    ):
        """RandomForestRegression Parameters"""
        self.params = {
            "model_name": model_name,
            "n_estimators": n_estimators,
            "random_state": random_state,
        }
        return self.params


class RandomForestRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """RandomForestRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class LogisticRegression(BaseBlock):
    def set_params(self, model_name: str, random_state: int = 0):
        """LogisticRegression Parameters"""
        self.params = {"model_name": model_name, "random_state": random_state}
        return self.params


class LogisticRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """LogisticRegressionPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class KNearestNeighbors(BaseBlock):
    def set_params(
        self,
        model_name: str,
        n_neighbors: int = 5,
        distance: str = "minkowski",
        p: int = 2,
        random_state: int = 0,
    ):
        """KNearestNeighbors Parameters"""
        self.params = {
            "model_name": model_name,
            "n_neighbors": n_neighbors,
            "distance": distance,
            "p": p,
            "random_state": random_state,
        }
        return self.params


class KNearestNeighborsPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """KNearestNeighborsPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class SupportVectorMachine(BaseBlock):
    def set_params(self, model_name: str):
        """SupportVectorMachine Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class SupportVectorMachinePredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """SupportVectorMachinePredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class KernelSupportVectorMachine(BaseBlock):
    def set_params(self, model_name: str, kernel: str = "rbf", random_state: int = 0):
        """KernelSupportVectorMachine Parameters"""
        self.params = {
            "model_name": model_name,
            "kernel": kernel,
            "random_state": random_state,
        }
        return self.params


class KernelSupportVectorMachinePredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """KernelSupportVectorMachinePredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class NaiveBayes(BaseBlock):
    def set_params(self, model_name: str):
        """NaiveBayes Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class NaiveBayesPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """NaiveBayesPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class DecisionTreeClassification(BaseBlock):
    def set_params(
        self, model_name: str, criterion: str = "gini", random_state: int = 0
    ):
        """DecisionTreeClassification Parameters"""
        self.params = {
            "model_name": model_name,
            "criterion": criterion,
            "random_state": random_state,
        }
        return self.params


class DecisionTreeClassificationPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """DecisionTreeClassificationPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class RandomForestClassification(BaseBlock):
    def set_params(self, model_name: str):
        """RandomForestClassification Parameters"""
        self.params = {
            "model_name": model_name,
        }
        return self.params


class RandomForestClassificationPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """RandomForestClassificationPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class HierarchicalClustering(BaseBlock):
    def set_params(
        self,
        model_name: str,
        n_clusters: int = 5,
        affinity: str = "euclidean",
        linkage: str = "ward",
    ):
        """HierarchichalClustering Parameters"""
        self.params = {
            "model_name": model_name,
            "n_clusters": n_clusters,
            "affinity": affinity,
            "linkage": linkage,
        }
        return self.params


class HierarchicalClusteringPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """HierarchichalClusteringPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class KMeansClustering(BaseBlock):
    def set_params(
        self,
        model_name: str,
        n_clusters: int = 5,
        init: str = "k-means++",
        random_state: int = 0,
    ):
        """KMeansClustering Parameters"""
        self.params = {
            "model_name": model_name,
            "n_clusters": n_clusters,
            "init": init,
            "random_state": random_state,
        }
        return self.params


class KMeansClusteringPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """KMeansClusteringPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class XGBoost(BaseBlock):
    def set_params(
        self,
        model_name: str,
    ):
        """XGBoost Parameters"""
        self.params = {
            "model_name": model_name,
        }
        return self.params


class XGBoostPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """XGBoostPredict Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params
