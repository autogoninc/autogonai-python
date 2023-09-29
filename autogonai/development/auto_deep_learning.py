from autogonai.development.base import BaseBlock, gen_params


class AutoImageClassifierInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoImageClassifierInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoImageClassifierTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoImageClassifierTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoTextClassifierInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoTextClassifierInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoTextClassifierTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoTextClassifierTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoStructuredDataClassifierInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoStructuredDataClassifierInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoStructuredDataClassifierTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoStructuredDataClassifierTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoImageRegressorInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoImageRegressorInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoImageRegressorTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoImageRegressorTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoTextRegressorInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoTextRegressorInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoTextRegressorTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoTextRegressorTrain Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoStructuredDataRegressorInit(BaseBlock):
    def set_params(self, hyp_params: dict):
        """AutoStructuredDataRegressorInit Parameters"""
        self.params = gen_params(locals())
        return self.params


class AutoStructuredDataRegressorTrain(BaseBlock):
    def set_params(self, model_name: str, hyp_params: dict):
        """AutoStructuredDataRegressorTrain Parameters"""
        self.params = gen_params(locals())
        return self.params
