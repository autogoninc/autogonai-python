from autogonai.api import API

class Client(API):
    from .functions import data_input
    from .functions import missing_data
    from .functions import feature_scaling
    from .functions import data_encode

    def __init__(self):
        pass
