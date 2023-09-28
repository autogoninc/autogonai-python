from autogonai.development.base import BaseBlock


def gen_params(arg_pairs):
    # Create an empty dictionary to store the arguments
    arguments_dict = {}

    # Get all local variables (including function arguments) as a dictionary
    local_variables = arg_pairs

    # Iterate through the local variables and store the arguments in the dictionary
    for key, value in local_variables.items():
        if key != "self":  # Exclude 'self' if it's a method within a class
            arguments_dict[key] = value

    return arguments_dict


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
        """InputData Parameters"""
        self.params = gen_params(locals())
        return self.params


class HandleMissingData(BaseBlock):
    def set_params(
        self,
        strategy_value: str,
        x_boundaries: str | None,
        y_boundaries: str | None,
    ):
        """HandleMissingData Parameters"""
        self.params = gen_params(locals())
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
        """EncodeData Parameters"""
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
        """SplitData Parameters"""
        self.params = gen_params(locals())
        return self.params


class FeatureScaleData(BaseBlock):
    def set_params(
        self,
        xtrain: bool,
        xtest: bool,
        x: bool,
        boundaries: str,
    ):
        """FeatureScaleData Parameters"""
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
        """DropColumns Parameters"""
        self.params = gen_params(locals())
        return self.params


class TimeStepData(BaseBlock):
    def set_params(
        self,
        timestep: int,
        y_value_source: bool,
    ):
        """TimeStepData Parameters"""
        self.params = gen_params(locals())
        return self.params


class FeatureSampling(BaseBlock):
    def set_params(
        self,
        dataset_url: str,
        x_boundaries,
        y_boundaries,
    ):
        self.params = gen_params(locals())
        return self.params


class ReshapeArray(BaseBlock):
    def set_params(
        self,
        data,
        dimensions,
    ):
        self.params = gen_params(locals())
        return self.params


class ScalarToNdarray(BaseBlock):
    def set_params(
        self,
        scalar,
        dimensions: int,
    ):
        self.params = gen_params(locals())
        return self.params


class ImageToNdarray(BaseBlock):
    def set_params(self, image_url: str, targe_size, rescale=True):
        self.params = gen_params(locals())
        return self.params


class ColumnsAstype(BaseBlock):
    def set_params(
        self,
        columns,
        astype: str,
    ):
        self.params = gen_params(locals())
        return self.params


class AutoDP(BaseBlock):
    def set_params(
        self,
        x_slice,
        y_slice,
        strategy_value,
        test_size_value,
        le_thresh,
        ohe_thresh,
        save_name,
        clean,
        dataset_type,
        load_name,
    ):
        self.params = gen_params(locals())

        return self.params


class TextVectorizer(BaseBlock):
    def set_params(
        self, vectorizer, boundariestoscale, dataset, xtrain, xtest, x, ytrain, ytest, y
    ):
        self.params = gen_params(locals())
        return self.params


class ParseDatetime(BaseBlock):
    def set_params(self, format, columns):
        self.params = gen_params(locals())
        return self.params


class ReorderColumn(BaseBlock):
    def set_params(self, order):
        self.params = gen_params(locals())
        return self.params


class ColumnAstype(BaseBlock):
    def set_params(self, dtype, columns):
        self.params = gen_params(locals())
        return self.params


class ShowDuplicates(BaseBlock):
    def set_params(self, columns):
        self.params = gen_params(locals())
        return self.params


class DropDuplicates(BaseBlock):
    def set_params(self, columns):
        self.params = gen_params(locals())
        return self.params


class DatasetInfo(BaseBlock):
    def set_params(self):
        self.params = gen_params(locals())
        return self.params


class DatasetCorrelations(BaseBlock):
    def set_params(self, method):
        self.params = gen_params(locals())
        return self.params


class DatasetDescription(BaseBlock):
    def set_params(self):
        self.params = gen_params(locals())
        return self.params


class DatasetUniques(BaseBlock):
    def set_params(self):
        self.params = gen_params(locals())
        return self.params


class StatsCounts(BaseBlock):
    def set_params(self, columns):
        self.params = gen_params(locals())
        return self.params


class PrincipalComponentAnalysis(BaseBlock):
    def set_params(self, n_components):
        self.params = gen_params(locals())
        return self.params


class Resampler(BaseBlock):
    def set_params(self, method):
        self.params = gen_params(locals())
        return self.params


class ScatterPlot(BaseBlock):
    def set_params(self, x, y):
        self.params = gen_params(locals())
        return self.params


class OrdinaryPlot(BaseBlock):
    def set_params(self, x, y):
        self.params = gen_params(locals())
        return self.params


class CompareScatterPlots(BaseBlock):
    def set_params(self, x1, y1, x2, y2):
        self.params = gen_params(locals())
        return self.params


class PiePlot(BaseBlock):
    def set_params(self, labels, values):
        self.params = gen_params(locals())
        return self.params


class HeatmapPlot(BaseBlock):
    def set_params(self, data):
        self.params = gen_params(locals())
        return self.params
