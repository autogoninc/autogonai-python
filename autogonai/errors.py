class Err(Exception):
    pass

class AutogonRequestError(Err):
    def __init__(self, status_code, error_message):
        # response status code
        self.status_code = status_code
        # the whole response header returned from API
        # self.header = header
        # error message returned from API
        self.error_message = error_message

class AutogonServerError(Err):
    def __init__(self, status_code, message):
        # response status code
        self.status_code = status_code
        # error message returned from API
        self.message = message
