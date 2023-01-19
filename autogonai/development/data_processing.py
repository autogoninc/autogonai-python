from autogonai.development.base import BaseBlock


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
        self.params = {
            'file_type': file_type,
            'dburl': dburl,
            'x_boundaries': x_boundaries,
            'y_boundaries': y_boundaries,
            'dbservertype': dbservertype,
            'dbpassword': dbpassword,
            'dbname': dbname,
            'query': query,
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

# def missing_data(self):
#     pass

# def feature_scaling(self):
#     pass

# def data_encode(self):
#     pass
