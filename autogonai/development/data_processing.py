# Import necessary libraries
from autogonai.development.base import BaseBlock, gen_params


# Define class DataInput
class DataInput(BaseBlock):
    def set_params(
        self,
        # file_type: str = None,
        # dburl: str = None,
        # x_boundaries: str = None,
        # y_boundaries: str = None,
        # dbservertype: str = None,
        # dbpassword: str = None,
        # dbname: str = None,
        # query: str = None,
        **kwargs
    ):
        """
        Sets parameters for DataInput class.

        Args:
            file_type (str, optional): Type of the input file. Defaults to None.
            dburl (str, optional): URL of the database. Defaults to None.
            x_boundaries (str, optional): X boundaries for data. Defaults to None.
            y_boundaries (str, optional): Y boundaries for data. Defaults to None.
            dbservertype (str, optional): Type of the database server. Defaults to None.
            dbpassword (str, optional): Password for the database. Defaults to None.
            dbname (str, optional): Name of the database. Defaults to None.
            query (str, optional): Query for database retrieval. Defaults to None.
            Other args can be found at: https://docs.autogon.ai/autogon-engine-studio/data-processing/data-input-dp_1

        Returns:
            dict: Parameters dictionary.
        """
        # self.params = gen_params(locals())
        self.params = kwargs
        return self.params


# Define class HandleMissingData
class HandleMissingData(BaseBlock):
    def set_params(
        self,
        strategy_value: str = None,
        boundaries: str | None = None,
    ):
        """
        Sets parameters for HandleMissingData class.

        Args:
            strategy_value (str, optional): Strategy for handling missing data. Defaults to None.
            boundaries (str, optional): Dataset boundaries for data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DataEncoding
class DataEncoding(BaseBlock):
    def set_params(
        self,
        dataset={"encode": False},
        xvalue={"encode": False},
        yvalue={"encode": False},
        save_name=None,
        load_name=None,
    ):
        """
        Sets parameters for DataEncoding class.

        Args:
            dataset (dict): Encoding Parameters for dataset variable
            xvalue (dict): Encoding Parameters for x variable
            yvalue (dict): Encoding Parameters for y variable
            save_name (optional): Save name for encoded data. Defaults to None.
            load_name (optional): Load name for encoded data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DataSplitting
class DataSplitting(BaseBlock):
    def set_params(self, test_size: float = None, random_state: int | None = None):
        """
        Sets parameters for DataSplitting class.

        Args:
            test_size (float, optional): Size of the test data. Defaults to None.
            random_state (int, optional): Random state for data splitting. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class FeatureScaling
class FeatureScaling(BaseBlock):
    def set_params(
        self,
        dataset: bool,
        xtrain: bool = None,
        xtest: bool = None,
        x: bool = None,
        ytrain: bool = None,
        ytest: bool = None,
        y: bool = None,
        boundariestoscale: str = None,
        save_name=None,
        load_name=None,
    ):
        """
        Sets parameters for FeatureScaling class.

        Args:
            xtrain (bool, optional): Flag for scaling X training data. Defaults to None.
            xtest (bool, optional): Flag for scaling X test data. Defaults to None.
            x (bool, optional): Flag for scaling X data. Defaults to None.
            ytrain (bool, optional): Flag for scaling Y training data. Defaults to None.
            ytest (bool, optional): Flag for scaling Y test data. Defaults to None.
            y (bool, optional): Flag for scaling Y data. Defaults to None.
            boundariestoscale (str, optional): Boundaries for scaling. Defaults to None.
            save_name (optional): Save name for scaled data. Defaults to None.
            load_name (optional): Load name for scaled data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DropColumns
class DropColumns(BaseBlock):
    def set_params(
        self,
        d_columns: list | None = None,
        x_columns: list | None = None,
        y_columns: list | None = None,
    ):
        """
        Sets parameters for DropColumns class.

        Args:
            d_columns (list, optional): Columns to drop from dataset. Defaults to None.
            x_columns (list, optional): Columns to drop from X data. Defaults to None.
            y_columns (list, optional): Columns to drop from Y data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class TimeStepData
class TimeStepData(BaseBlock):
    def set_params(
        self,
        index: int,
        lookback: int,
        lookforward: int = 1,
    ):
        """
        Sets parameters for TimeStepData class.

        Args:
            index (int): Column index in the dataset
            lookback (int): The lookback value. Defaults to None.
            lookback (int, optional): The lookforward value. Defaults to 1.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class FeatureSampling
class FeatureSampling(BaseBlock):
    def set_params(
        self,
        dataset_url: str = None,
        x_boundaries=None,
        y_boundaries=None,
    ):
        """
        Sets parameters for FeatureSampling class.

        Args:
            dataset_url (str, optional): URL of the dataset. Defaults to None.
            x_boundaries (optional): X boundaries for data sampling. Defaults to None.
            y_boundaries (optional): Y boundaries for data sampling. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ReshapeArray
class ReshapeArray(BaseBlock):
    def set_params(
        self,
        data=None,
        dimensions=None,
    ):
        """
        Sets parameters for ReshapeArray class.

        Args:
            data (optional): Data to reshape. Defaults to None.
            dimensions (optional): Dimensions for reshaping. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ScalarToNdarray
class ScalarToNdarray(BaseBlock):
    def set_params(
        self,
        scalar=None,
        dimensions: int = None,
    ):
        """
        Sets parameters for ScalarToNdarray class.

        Args:
            scalar (optional): Scalar value to convert to ndarray. Defaults to None.
            dimensions (int, optional): Dimensions of the ndarray. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ImageToNdarray
class ImageToNdarray(BaseBlock):
    def set_params(self, image_url: str = None, targe_size=None, rescale: bool = True):
        """
        Sets parameters for ImageToNdarray class.

        Args:
            image_url (str, optional): URL of the image. Defaults to None.
            targe_size (optional): Target size for the image. Defaults to None.
            rescale (bool, optional): Flag for image rescaling. Defaults to True.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ColumnsAstype
class ColumnsAstype(BaseBlock):
    def set_params(
        self,
        columns=None,
        astype: str = None,
    ):
        """
        Sets parameters for ColumnsAstype class.

        Args:
            columns (optional): Columns to apply astype conversion. Defaults to None.
            astype (str, optional): Data type for the conversion. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class AutoDP
class AutoDP(BaseBlock):
    def set_params(
        self,
        x_slice=None,
        y_slice=None,
        strategy_value=None,
        test_size_value=None,
        le_thresh=None,
        ohe_thresh=None,
        save_name=None,
        clean=None,
        dataset_type=None,
        load_name=None,
    ):
        """
        Sets parameters for AutoDP class.

        Args:
            x_slice (optional): X data slice. Defaults to None.
            y_slice (optional): Y data slice. Defaults to None.
            strategy_value (optional): Strategy for data processing. Defaults to None.
            test_size_value (optional): Size of the test data. Defaults to None.
            le_thresh (optional): Threshold for Label Encoding. Defaults to None.
            ohe_thresh (optional): Threshold for One-Hot Encoding. Defaults to None.
            save_name (optional): Save name for processed data. Defaults to None.
            clean (optional): Data cleaning flag. Defaults to None.
            dataset_type (optional): Type of the dataset. Defaults to None.
            load_name (optional): Load name for processed data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class TextVectorizer
class TextVectorizer(BaseBlock):
    def set_params(
        self,
        vectorizer=None,
        boundariestoscale=None,
        dataset=None,
        xtrain=None,
        xtest=None,
        x=None,
        ytrain=None,
        ytest=None,
        y=None,
        save_name=None,
        load_name=None,
    ):
        """
        Sets parameters for TextVectorizer class.

        Args:
            vectorizer (optional): Text vectorizer. Defaults to None.
            boundariestoscale (optional): Boundaries for scaling. Defaults to None.
            dataset (optional): Dataset. Defaults to None.
            xtrain (optional): X training data. Defaults to None.
            xtest (optional): X test data. Defaults to None.
            x (optional): X data. Defaults to None.
            ytrain (optional): Y training data. Defaults to None.
            ytest (optional): Y test data. Defaults to None.
            y (optional): Y data. Defaults to None.
            save_name (optional): Save name for processed data. Defaults to None.
            load_name (optional): Load name for processed data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ParseDatetime
class ParseDatetime(BaseBlock):
    def set_params(self, index=None, drop=None):
        """
        Sets parameters for ParseDatetime class.

        Args:
            index (optional): Index for date parsing. Defaults to None.
            drop (optional): Drop flag for date parsing. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ReorderColumn
class ReorderColumn(BaseBlock):
    def set_params(
        self,
        column=None,
        posititon=None,
        dataset=None,
        xtrain=None,
        xtest=None,
        x=None,
        ytrain=None,
        ytest=None,
        y=None,
    ):
        """
        Sets parameters for ReorderColumn class.

        Args:
            column (optional): Column to reorder. Defaults to None.
            posititon (optional): New position for the column. Defaults to None.
            dataset (optional): Dataset. Defaults to None.
            xtrain (optional): X training data. Defaults to None.
            xtest (optional): X test data. Defaults to None.
            x (optional): X data. Defaults to None.
            ytrain (optional): Y training data. Defaults to None.
            ytest (optional): Y test data. Defaults to None.
            y (optional): Y data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ColumnAstype
class ColumnAstype(BaseBlock):
    def set_params(self, astype=None, columns=None):
        """
        Sets parameters for ColumnAstype class.

        Args:
            astype (optional): Data type for columns. Defaults to None.
            columns (optional): Columns to convert. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ShowDuplicates
class ShowDuplicates(BaseBlock):
    def set_params(self, columns=None):
        """
        Sets parameters for ShowDuplicates class.

        Args:
            columns (optional): Columns to check for duplicates. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DropDuplicates
class DropDuplicates(BaseBlock):
    def set_params(self, columns=None):
        """
        Sets parameters for DropDuplicates class.

        Args:
            columns (optional): Columns to drop duplicates. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DatasetInfo
class DatasetInfo(BaseBlock):
    def set_params(self):
        """
        Sets parameters for DatasetInfo class.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DatasetCorrelations
class DatasetCorrelations(BaseBlock):
    def set_params(self):
        """
        Sets parameters for DatasetCorrelations class.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DatasetDescription
class DatasetDescription(BaseBlock):
    def set_params(self):
        """
        Sets parameters for DatasetDescription class.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class DatasetUniques
class DatasetUniques(BaseBlock):
    def set_params(self):
        """
        Sets parameters for DatasetUniques class.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class StatsCounts
class StatsCounts(BaseBlock):
    def set_params(self, index=None):
        """
        Sets parameters for StatsCounts class.

        Args:
            index (optional): Index for stats counting. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class PrincipalComponentAnalysis
class PrincipalComponentAnalysis(BaseBlock):
    def set_params(
        self,
        n_components=None,
        dataset=None,
        xtrain=None,
        xtest=None,
        x=None,
        ytrain=None,
        ytest=None,
        y=None,
        save_name=None,
        load_name=None,
    ):
        """
        Sets parameters for PrincipalComponentAnalysis class.

        Args:
            n_components (optional): Number of components for PCA. Defaults to None.
            dataset (optional): Dataset. Defaults to None.
            xtrain (optional): X training data. Defaults to None.
            xtest (optional): X test data. Defaults to None.
            x (optional): X data. Defaults to None.
            ytrain (optional): Y training data. Defaults to None.
            ytest (optional): Y test data. Defaults to None.
            y (optional): Y data. Defaults to None.
            save_name (optional): Save name for PCA data. Defaults to None.
            load_name (optional): Load name for PCA data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class Resampler
class Resampler(BaseBlock):
    def set_params(
        self,
        xy=None,
        xy_train=None,
        xy_test=None,
        resampler=None,
        save_name=None,
        load_name=None,
    ):
        """
        Sets parameters for Resampler class.

        Args:
            xy (optional): Data for resampling. Defaults to None.
            xy_train (optional): Training data for resampling. Defaults to None.
            xy_test (optional): Test data for resampling. Defaults to None.
            resampler (optional): Resampling strategy. Defaults to None.
            save_name (optional): Save name for resampled data. Defaults to None.
            load_name (optional): Load name for resampled data. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class ScatterPlot
class ScatterPlot(BaseBlock):
    def set_params(self, xvalue=None, yvalue=None, is_grid=None):
        """
        Sets parameters for ScatterPlot class.

        Args:
            xvalue (optional): X values for the plot. Defaults to None.
            yvalue (optional): Y values for the plot. Defaults to None.
            is_grid (optional): Grid flag for the plot. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class OrdinaryPlot
class OrdinaryPlot(BaseBlock):
    def set_params(self, xvalue=None, yvalue=None, is_grid=None):
        """
        Sets parameters for OrdinaryPlot class.

        Args:
            xvalue (optional): X values for the plot. Defaults to None.
            yvalue (optional): Y values for the plot. Defaults to None.
            is_grid (optional): Grid flag for the plot. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class CompareScatterPlots
class CompareScatterPlots(BaseBlock):
    def set_params(
        self,
        avalue=None,
        bvalue=None,
        xvalue=None,
        yvalue=None,
        is_grid=None,
    ):
        """
        Sets parameters for CompareScatterPlots class.

        Args:
            avalue (optional): Data A for the plot. Defaults to None.
            bvalue (optional): Data B for the plot. Defaults to None.
            xvalue (optional): X values for the plot. Defaults to None.
            yvalue (optional): Y values for the plot. Defaults to None.
            is_grid (optional): Grid flag for the plot. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class PiePlot
class PiePlot(BaseBlock):
    def set_params(self, dataset=None):
        """
        Sets parameters for PiePlot class.

        Args:
            dataset (optional): Dataset for the pie plot. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params


# Define class HeatmapPlot
class HeatmapPlot(BaseBlock):
    def set_params(self, dataset=None):
        """
        Sets parameters for HeatmapPlot class.

        Args:
            dataset (optional): Dataset for the heatmap plot. Defaults to None.

        Returns:
            dict: Parameters dictionary.
        """
        self.params = gen_params(locals())
        return self.params
