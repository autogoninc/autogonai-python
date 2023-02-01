from autogonai.development.base import BaseBlock


class InputData(BaseBlock):
    def set_params(
        self,
        file_type: str,
        dburl: str,
        x_boundaries: str,
        y_boundaries: str,
        dbservertype: str = "",
        dbpassword: str = "",
        dbname: str = "",
        query: str = "",
    ):
        self.params = {
            "file_type": file_type,
            "dburl": dburl,
            "x_boundaries": x_boundaries,
            "y_boundaries": y_boundaries,
            "dbservertype": dbservertype,
            "dbpassword": dbpassword,
            "dbname": dbname,
            "query": query,
        }
        return self.params


class HandleMissingData(BaseBlock):
    def set_params(
        self,
        strategy_value: str,
        x_boundaries: str | None,
        y_boundaries: str | None,
    ):
        '''HandleMissingData'''
        self.params = {
            "strategy_value": strategy_value,
            "x_boundaries": x_boundaries,
            "y_boundaries": y_boundaries,
        }
        return self.params


class EncodeData(BaseBlock):
    def set_params(
        self,
        x_encoding_type: str,
        x_index: int,
        y_encoding_type: str,
        y_index: int,
        y_remainder: str | None = None,
        x_remainder: str | None = None,
    ):
        x_encode = True if not x_encoding_type == None else False
        y_encode = True if not y_encoding_type == None else False
        self.params = {
            "xvalue": {
                "encode": x_encode,
                "encoding_type": x_encoding_type,
                "remainder": x_remainder,
                "index": x_index,
            },
            "yvalue": {
                "encode": y_encode,
                "encoding_type": y_encoding_type,
                "remainder": y_remainder,
                "index": y_index,
            },
        }
        return self.params


class SplitData(BaseBlock):
    def set_params(self, test_size: float, random_state: int | None = None):
        self.params = {
            "test_size": test_size,
            "random_state": random_state,
        }
        return self.params


class FeatureScaleData(BaseBlock):
    def set_params(
        self,
        xtrain: bool,
        xtest: bool,
        x: bool,
        boundaries: str,
    ):
        self.params = {
            "xtrain": xtrain,
            "xtest": xtest,
            "x": x,
            "boundariestoscale": boundaries,
        }
        return self.params

class DropColumns(BaseBlock):
    def set_params(
        self,
        x_columns: list | None,
        y_columns: list | None,
    ):
        self.params = {
            'x_columns': x_columns,
            'y_columns': y_columns,
        }
        return self.params

class TimeStepData(BaseBlock):
    def set_params(
        self,
        timestep: int,
        y_value_source: bool,
    ):
        self.params = {
            "timestep": timestep,
            "y_value_source": y_value_source,
        }
        return self.params
