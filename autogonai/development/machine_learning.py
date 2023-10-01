from autogonai.development.base import BaseBlock, gen_params


class PredictBlock(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """SimpleLinearRegressionPredict Parameters"""
        self.params = gen_params(locals())
        return self.params


class MetricsBlock(BaseBlock):
    def set_params(self, model_name: str, metric: str):
        """SimpleLinearRegressionPredict Parameters"""
        self.params = gen_params(locals())
        return self.params


class SimpleLinearRegression(BaseBlock):
    def set_params(self, model_name: str):
        """SimpleLinearRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class SimpleLinearRegressionPredict(PredictBlock):
    pass


class SimpleLinearRegressionMetrics(MetricsBlock):
    pass


class MultipleLinearRegression(BaseBlock):
    def set_params(self, model_name: str):
        """SimpleLinearRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class MultipleLinearRegressionPredict(PredictBlock):
    pass


class MultipleLinearRegressionMetrics(MetricsBlock):
    pass


class PolynomialLinearRegression(BaseBlock):
    def set_params(self, model_name: str, degree: int = 2):
        """PolynomialLinearRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class PolynomialLinearRegressionPredict(PredictBlock):
    pass


class PolynomialLinearRegressionMetrics(MetricsBlock):
    pass


class SupportVectorRegression(BaseBlock):
    def set_params(self, model_name: str, kernel: str = "rbf"):
        """SupportVectorRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class SupportVectorRegressionPredict(PredictBlock):
    pass


class SupportVectorRegressionMetrics(MetricsBlock):
    pass


class DecisionTreeRegression(BaseBlock):
    def set_params(self, model_name: str, random_state: int = 0):
        """DecisionTreeRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class DecisionTreeRegressionPredict(PredictBlock):
    pass


class DecisionTreeRegressionMetrics(MetricsBlock):
    pass


class RandomForestRegression(BaseBlock):
    def set_params(
        self, model_name: str, n_estimators: int = 100, random_state: int = 0
    ):
        """RandomForestRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class RandomForestRegressionPredict(PredictBlock):
    pass


class RandomForestRegressionMetrics(MetricsBlock):
    pass


class LogisticRegression(BaseBlock):
    def set_params(self, model_name: str, random_state: int = 0):
        """LogisticRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class LogisticRegressionPredict(PredictBlock):
    pass


class LogisticRegressionMetrics(MetricsBlock):
    pass


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
        self.params = gen_params(locals())
        return self.params


class KNearestNeighborsPredict(PredictBlock):
    pass


class KNearestNeighborsMetrics(MetricsBlock):
    pass


class SupportVectorMachine(BaseBlock):
    def set_params(self, model_name: str):
        """SupportVectorMachine Parameters"""
        self.params = gen_params(locals())
        return self.params


class SupportVectorMachinePredict(PredictBlock):
    pass


class SupportVectorMachineMetrics(MetricsBlock):
    pass


class KernelSupportVectorMachine(BaseBlock):
    def set_params(self, model_name: str, kernel: str = "rbf", random_state: int = 0):
        """KernelSupportVectorMachine Parameters"""
        self.params = gen_params(locals())
        return self.params


class KernelSupportVectorMachinePredict(PredictBlock):
    pass


class KernelSupportVectorMachineMetrics(MetricsBlock):
    pass


class NaiveBayes(BaseBlock):
    def set_params(self, model_name: str):
        """NaiveBayes Parameters"""
        self.params = gen_params(locals())
        return self.params


class NaiveBayesPredict(PredictBlock):
    pass


class NaiveBayesMetrics(MetricsBlock):
    pass


class DecisionTreeClassification(BaseBlock):
    def set_params(
        self, model_name: str, criterion: str = "gini", random_state: int = 0
    ):
        """DecisionTreeClassification Parameters"""
        self.params = gen_params(locals())
        return self.params


class DecisionTreeClassificationPredict(PredictBlock):
    pass


class DecisionTreeClassificationMetrics(MetricsBlock):
    pass


class RandomForestClassification(BaseBlock):
    def set_params(self, model_name: str):
        """RandomForestClassification Parameters"""
        self.params = gen_params(locals())
        return self.params


class RandomForestClassificationPredict(PredictBlock):
    pass


class RandomForestClassificationMetrics(MetricsBlock):
    pass


class HierarchicalClustering(BaseBlock):
    def set_params(
        self,
        model_name: str,
        n_clusters: int = 5,
        affinity: str = "euclidean",
        linkage: str = "ward",
    ):
        """HierarchichalClustering Parameters"""
        self.params = gen_params(locals())
        return self.params


class HierarchicalClusteringPredict(PredictBlock):
    pass


class HierarchicalClusteringMetrics(MetricsBlock):
    pass


class KMeansClustering(BaseBlock):
    def set_params(
        self,
        model_name: str,
        n_clusters: int = 5,
        init: str = "k-means++",
        random_state: int = 0,
    ):
        """KMeansClustering Parameters"""
        self.params = gen_params(locals())
        return self.params


class KMeansClusteringPredict(PredictBlock):
    pass


class KMeansClusteringMetrics(MetricsBlock):
    pass


class XGBoost(BaseBlock):
    def set_params(
        self,
        model_name: str,
    ):
        """XGBoost Parameters"""
        self.params = gen_params(locals())
        return self.params


class XGBoostPredict(PredictBlock):
    pass


class XGBoostMetrics(MetricsBlock):
    pass


class GridSearch(BaseBlock):
    def set_params(
        self,
        model_name: str,
        param_grid: list,
    ):
        """GridSearch Parameters"""
        self.params = gen_params(locals())
        return self.params


class SHAPExplain(BaseBlock):
    def set_params(
        self,
        model_name: str,
    ):
        """SHAPExplain Parameters"""
        self.params = gen_params(locals())
        return self.params


class IsolationForest(BaseBlock):
    def set_params(
        self,
        model_name: str,
        random_state: int,
    ):
        """IsolationForest Parameters"""
        self.params = gen_params(locals())
        return self.params


class IsolationForestPredict(PredictBlock):
    pass


class IsolationForestMetrics(MetricsBlock):
    pass


class DBScanClustering(BaseBlock):
    def set_params(self, eps, min_samples, metric):
        """DBScanClustering Parameters"""
        self.params = gen_params(locals())
        return self.params


class DBScanClusteringPredict(PredictBlock):
    pass
