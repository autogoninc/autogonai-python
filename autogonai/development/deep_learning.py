from autogonai.development.base import BaseBlock, gen_params


class ArtificialNeuralNetworkInit(BaseBlock):
    def set_params(self, layer_list: list):
        """ArtificialNeuralNetworkInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class ArtificialNeuralNetworkTrain(BaseBlock):
    def set_params(self, model_name: str, add_dim: bool, hyp_params: dict):
        """ArtificialNeuralNetworkTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class ArtificialNeuralNetworkEvaluate(BaseBlock):
    def set_params(self, hyp_params: dict):
        """ArtificialNeuralNetworkEvaluate Parameters"""
        self.params = gen_params(locals())
        return self.params


class ArtificialNeuralNetworkPredict(BaseBlock):
    def set_params(self, test_data: str, hyp_params: dict):
        """ArtificialNeuralNetworkPredict Parameters"""
        self.params = gen_params(locals())
        return self.params


class SelfOrganizingMapsInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """SelfOrganizingMapsInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class SelfOrganizingMapsTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """SelfOrganizingMapsTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class SelfOrganizingMapsPredict(BaseBlock):
    def set_params(self, test_data: str, row: int):
        """SelfOrganizingMapsPredict Parameters"""
        self.params = {"test_data": test_data, "row": row}
        return self.params


class RestrictedBoltzmannMachineInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """RestrictedBoltzmannMachineInit Parameters"""
        self.params = {"hyp_params": hyp_params, "flowjson": []}
        return self.params


class RestrictedBoltzmannMachineTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """RestrictedBoltzmannMachineTrain Parameters"""
        self.params = {
            "model_name": model_name,
            "hyp_params": hyp_params,
            "flowjson": [],
        }
        return self.params


class RestrictedBoltzmannMachineTransform(BaseBlock):
    def set_params(self, test_data: str):
        """RestrictedBoltzmannMachineTransform Parameters"""
        self.params = {"test_data": test_data}
        return self.params


class AutoImageClassifierInit(BaseBlock):
    def set_params(self, max_trials: int):
        """AutoImageClassifierInit Parameters"""
        self.params = {"max_trials": max_trials, "flowjson": []}
        return self.params


class AutoImageClassifierTrain(BaseBlock):
    def set_params(self, train_data_block: int, model_name: str, hyp_params: dict):
        """AutoImageClassifierTrain Parameters"""
        self.params = {
            "train_data_block": train_data_block,
            "model_name": model_name,
            "hyp_params": hyp_params,
            "flowjson": [],
        }
        return self.params


class AutoTextClassifierInit(BaseBlock):
    def set_params(self, max_trials: int):
        """AutoTextClassifierInit Parameters"""
        self.params = {"max_trials": max_trials, "flowjson": []}
        return self.params


class AutoTextClassifierTrain(BaseBlock):
    def set_params(self, train_data_block: int, model_name: str, hyp_params: dict):
        """AutoTextClassifierTrain Parameters"""
        self.params = {
            "train_data_block": train_data_block,
            "model_name": model_name,
            "hyp_params": hyp_params,
            "flowjson": [],
        }
        return self.params


class AutoStructuredDataClassifierInit(BaseBlock):
    def set_params(self, max_trials: int):
        """AutoStructuredDataClassifierInit Parameters"""
        self.params = {"max_trials": max_trials, "flowjson": []}
        return self.params


class AutoStructuredDataClassifierTrain(BaseBlock):
    def set_params(self, train_data_block: int, model_name: str, hyp_params: dict):
        """AutoStructuredDataClassifierTrain Parameters"""
        self.params = {
            "train_data_block": train_data_block,
            "model_name": model_name,
            "hyp_params": hyp_params,
            "flowjson": [],
        }
        return self.params
