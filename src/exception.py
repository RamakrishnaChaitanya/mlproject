import sys # to manipulate the duuferent parts of the python runtime environment
from src.logger import logging

# common the entire project

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = "Error occured in python script named [{0}] line number [{1}] error message [{2}]".format(file_name,
                                                                                                           line_no,
                                                                                                           error)
    return error_msg

class CustomException(Exception): # custom exception class inheriting from exception class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # because of inheriting the exception classs (base class)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ =="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Logging has started")
        raise CustomException(e, sys)
