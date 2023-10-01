# Import necessary libraries
from autogonai.development.base import BaseBlock, gen_params


# Define class AutoRegression
class AutoRegression(BaseBlock):
    def set_params(
        self,
        model_name: str = None,
        time_left: int = None,
        run_time_limit: int = None,
        n_jobs: int = None,
    ):
        """
        Sets parameters for AutoRegression class.

        Args:
            model_name (str, optional): Name of the regression model. Defaults to None.
            time_left (int, optional): Time left for the regression. Defaults to None.
            run_time_limit (int, optional): Time limit for the regression run. Defaults to None.
            n_jobs (int, optional): Number of jobs for the regression. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoRegressionPredict
class AutoRegressionPredict(BaseBlock):
    def set_params(self, model_name: str = None):
        """
        Sets parameters for AutoRegressionPredict class.

        Args:
            model_name (str, optional): Name of the regression model. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoRegressionMetrics
class AutoRegressionMetrics(BaseBlock):
    def set_params(self, model_name: str = None, metric: str = None):
        """
        Sets parameters for AutoRegressionMetrics class.

        Args:
            model_name (str, optional): Name of the regression model. Defaults to None.
            metric (str, optional): Metric for regression evaluation. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoClassification
class AutoClassification(BaseBlock):
    def set_params(
        self,
        model_name: str = None,
        time_left: int = None,
        run_time_limit: int = None,
        n_jobs: int = None,
    ):
        """
        Sets parameters for AutoClassification class.

        Args:
            model_name (str, optional): Name of the classification model. Defaults to None.
            time_left (int, optional): Time left for the classification. Defaults to None.
            run_time_limit (int, optional): Time limit for the classification run. Defaults to None.
            n_jobs (int, optional): Number of jobs for the classification. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoClassificationPredict
class AutoClassificationPredict(BaseBlock):
    def set_params(self, model_name: str = None):
        """
        Sets parameters for AutoClassificationPredict class.

        Args:
            model_name (str, optional): Name of the classification model. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoClassificationMetrics
class AutoClassificationMetrics(BaseBlock):
    def set_params(self, model_name: str = None, metric: str = None):
        """
        Sets parameters for AutoClassificationMetrics class.

        Args:
            model_name (str, optional): Name of the classification model. Defaults to None.
            metric (str, optional): Metric for classification evaluation. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params
