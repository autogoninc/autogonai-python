class ArtificialNeuralNetworkInit(BaseBlock):
    def set_params(self, layer_list: list):
        """ArtificialNeuralNetworkInit Parameters"""
        self.params = {"layer_list": layer_list}
        return self.params


class ArtificialNeuralNetworkTrain(BaseBlock):
    def set_params(self, train_data_block: int, model_save_name: str, hyp_params: dict):
        """ArtificialNeuralNetworkTrain Parameters"""
        self.params = {
            "train_data_block": train_data_block,
            "model_save_name": model_save_name,
            "hyp_params": hyp_params,
        }
        return self.params


class ArtificialNeuralNetworkEvaluate(BaseBlock):
    def set_params(self, test_data_block: int, hyp_params: dict):
        """ArtificialNeuralNetworkEvaluate Parameters"""
        self.params = {
            "test_data_block": test_data_block,
            "hyp_params": hyp_params,
        }
        return self.params


class ArtificialNeuralNetworkPredict(BaseBlock):
    def set_params(self, x_url: str, hyp_params: dict):
        """ArtificialNeuralNetworkPredict Parameters"""
        self.params = {
            "x_url": x_url,
            "hyp_params": hyp_params,
        }
        return self.params


class SelfOrganizingMapsInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """SelfOrganizingMapsInit Parameters"""
        self.params = {"hyp_params": hyp_params}
        return self.params


class SelfOrganizingMapsTrain(BaseBlock):
    def set_params(self, model_save_name: str, hyp_params: dict):
        """SelfOrganizingMapsTrain Parameters"""
        self.params = {"model_save_name": model_save_name, "hyp_params": hyp_params}
        return self.params


class SelfOrganizingMapsPredict(BaseBlock):
    def set_params(self, x_url: str, row: int):
        """SelfOrganizingMapsPredict Parameters"""
        self.params = {"x_url": x_url, "row": row}
        return self.params


class RestrictedBoltzmannMachineInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """RestrictedBoltzmannMachineInit Parameters"""
        self.params = {"hyp_params": hyp_params}
        return self.params


class RestrictedBoltzmannMachineTrain(BaseBlock):
    def set_params(self, model_save_name: str, hyp_params: dict):
        """RestrictedBoltzmannMachineTrain Parameters"""
        self.params = {"model_save_name": model_save_name, "hyp_params": hyp_params}
        return self.params


class RestrictedBoltzmannMachineTransform(BaseBlock):
    def set_params(self, x_url: str):
        """RestrictedBoltzmannMachineTransform Parameters"""
        self.params = {"x_url": x_url}
        return self.params
