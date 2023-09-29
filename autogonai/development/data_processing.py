from autogonai.development.base import BaseBlock, gen_params


class DataInput(BaseBlock):
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
        """DataInput Parameters"""
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


class DataEncoding(BaseBlock):
    def set_params(
        self,
        x_encoding_type: str = None,
        x_index: int = 0,
        y_encoding_type: str = None,
        y_index: int = 0,
        y_remainder: str | None = None,
        x_remainder: str | None = None,
        save_name=None,
        load_name=None,
    ):
        """DataEncoding Parameters"""
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
            "save_name": save_name,
            "load_name": load_name,
        }
        return self.params


class DataSplitting(BaseBlock):
    def set_params(self, test_size: float, random_state: int | None = None):
        """DataSplitting Parameters"""
        self.params = gen_params(locals())
        return self.params


class FeatureScaling(BaseBlock):
    def set_params(
        self,
        xtrain: bool,
        xtest: bool,
        x: bool,
        boundariestoscale: str,
        save_name,
        load_name,
    ):
        """FeatureScaleData Parameters"""
        self.params = gen_params(locals())
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
        self,
        vectorizer,
        boundariestoscale,
        dataset,
        xtrain,
        xtest,
        x,
        ytrain,
        ytest,
        y,
        save_name,
        load_name,
    ):
        self.params = gen_params(locals())
        return self.params


class ParseDatetime(BaseBlock):
    def set_params(self, index, drop):
        self.params = gen_params(locals())
        return self.params


class ReorderColumn(BaseBlock):
    def set_params(
        self, column, posititon, dataset, xtrain, xtest, x, ytrain, ytest, y
    ):
        self.params = gen_params(locals())
        return self.params


class ColumnAstype(BaseBlock):
    def set_params(self, astype, columns):
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
    def set_params(self):
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
    def set_params(self, index):
        self.params = gen_params(locals())
        return self.params


class PrincipalComponentAnalysis(BaseBlock):
    def set_params(
        self,
        n_components,
        dataset,
        xtrain,
        xtest,
        x,
        ytrain,
        ytest,
        y,
        save_name,
        load_name,
    ):
        self.params = gen_params(locals())
        return self.params


class Resampler(BaseBlock):
    def set_params(self, xy, xy_train, xy_test, resampler, save_name, load_name):
        self.params = gen_params(locals())
        return self.params


class ScatterPlot(BaseBlock):
    def set_params(self, xvalue, yvalue, is_grid):
        self.params = gen_params(locals())
        return self.params


class OrdinaryPlot(BaseBlock):
    def set_params(self, xvalue, yvalue, is_grid):
        self.params = gen_params(locals())
        return self.params


class CompareScatterPlots(BaseBlock):
    def set_params(self, avalue, bvalue, xvalue, yvalue, is_grid):
        self.params = gen_params(locals())
        return self.params


class PiePlot(BaseBlock):
    def set_params(self, dataset):
        self.params = gen_params(locals())
        return self.params


class HeatmapPlot(BaseBlock):
    def set_params(self, dataset):
        self.params = gen_params(locals())
        return self.params
