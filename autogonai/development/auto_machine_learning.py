from autogonai.development.base import BaseBlock, gen_params


class AutoRegression(BaseBlock):
    def set_params(self, model_name: str, time_left, run_time_limit, n_jobs):
        """AutoRegression Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoRegressionPredict(BaseBlock):
    def set_params(self, model_name: str):
        """AutoRegressionPredict Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoRegressionMetrics(BaseBlock):
    def set_params(self, model_name: str, metric: str):
        """AutoRegressionMetrics Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoClassification(BaseBlock):
    def set_params(self, model_name: str, time_left, run_time_limit, n_jobs):
        """AutoClassification Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoClassificationPredict(BaseBlock):
    def set_params(self, model_name: str):
        """AutoClassificationPredict Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoClassificationMetrics(BaseBlock):
    def set_params(self, model_name: str, metric: str):
        """AutoClassificationMetrics Parameters"""
        self.params = gen_params(locals())
        return self.params
