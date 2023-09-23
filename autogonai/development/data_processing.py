from autogonai.development.base import BaseBlock

from typing import Any, Optional


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
        '''InputData Parameters'''
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
        '''HandleMissingData Parameters'''
        self.params = {
            "strategy_value": strategy_value,
            "x_boundaries": x_boundaries,
            "y_boundaries": y_boundaries,
        }
        return self.params


class EncodeData(BaseBlock):
    def set_params(
        self,
        x_encoding_type: str = None,
        x_index: int = 0,
        y_encoding_type: str = None,
        y_index: int = 0,
        y_remainder: str | None = None,
        x_remainder: str | None = None,
    ):
        '''EncodeData Parameters'''
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
        '''SplitData Parameters'''
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
        '''FeatureScaleData Parameters'''
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
        '''DropColumns Parameters'''
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
        '''TimeStepData Parameters'''
        self.params = {
            "timestep": timestep,
            "y_value_source": y_value_source,
        }
        return self.params

class FeatureSampleData(BaseBlock):
    def set_params(
            self,
            dataset_url: str,
            x_boundaries: tuple, 
            y_boundaries: tuple,
    ):
        self.params = {
            "dataset_url": dataset_url,
            "x_boundaries": x_boundaries,
            "y_boundaries": y_boundaries
        }
        return self.params
    
class ReshapeArray(BaseBlock):
    def set_params(
            self,
            dataset_url: str,
            dimensions: tuple,
    ):
        self.params = {
            "dataset_url": dataset_url,
            "dimensions": dimensions,
        } 
        return self.params
    
class ScalarToNdarray(BaseBlock):
    def set_params(
            self,
            scalar: Optional(Any), 
            ndims: Optional(Any),
    ):
        self.params = {
            "scalar": scalar,
            "ndims": ndims,
        } 
        return self.params
    
class ImageToNdarray(BaseBlock):
    def set_params(
            self,
            image: str, 
            size: Optional(Any),
    ):
        self.params = {
            "image": image,
            "size": size,
        } 
        return self.params
    
class ColumnsAstype(BaseBlock):
    def set_params(
            self,
            dataset_url: str,
            column_indices: Optional(Any),
            datatype: Optional(str),
    ):
        self.params = {
            "dataset_url": dataset_url,
            "column_indices": column_indices,
            "datatype": datatype,
        } 
        return self.params
    
class AutoDP(BaseBlock):
    def set_params(
            self,
    ):
        self.params = {}
        return self.params
    
class TextVectorizer(BaseBlock):
    def set_params(
            self,

    ):
        self.params = {}
        return self.params