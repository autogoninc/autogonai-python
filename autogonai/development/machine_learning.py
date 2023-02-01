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
        """MultipleLinearRegression Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class PolynomialLinearRegression(BaseBlock):
    def set_params(self, model_name: str):
        """PolynomialLinearRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class PolynomialLinearRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """PolynomialLinearRegression Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class SupportVectorRegression(BaseBlock):
    def set_params(self, model_name: str):
        """SupportVectorRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class SupportVectorRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """SupportVectorRegression Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class DecisionTreeRegression(BaseBlock):
    def set_params(self, model_name: str):
        """DecisionTreeRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class DecisionTreeRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """DecisionTreeRegression Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params


class RandomForestRegression(BaseBlock):
    def set_params(self, model_name: str):
        """RandomForestRegression Parameters"""
        self.params = {"model_name": model_name}
        return self.params


class RandomForestRegressionPredict(BaseBlock):
    def set_params(self, model_name: str, test_data: str):
        """RandomForestRegression Parameters"""
        self.params = {"model_name": model_name, "test_data": test_data}
        return self.params
