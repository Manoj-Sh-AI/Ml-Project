# Whenever any error message is occured, whenever inside the catch block we raize custom exception, the message will be returned 
# Error occured in this python script_name, in this line_number

import sys # It allows you to interact with the Python runtime environment and perform tasks related to system and program execution
import logging
from logger import logging

def error_message_detail(error, error_detail:sys): # sys containd error related details
    _, _, exc_tb = error_detail.exc_info() # exc_info() -> Execution Info, it gives 3 important info where the first 2 info is not relative to this senario
                                           # exc_tb -> It gives on which file the exception has occured and on which line number it has occured

    file_name = exc_tb.tb_frame.f_code.co_filename  # Gives the file name -> code is given in Python Custom exception handeling Documentation

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format( file_name, exc_tb.tb_lineno, str(error))  # These are:- file_name, line_number, error_message 
                     # [{0}], [{1}], [{2}] -> place holders 

    return error_message


class CustomException(Exception): # exception class named CustomException that inherits from the built-in Exception class

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # This line calls the constructor of the parent class (Exception) using the super() function. It initializes the exception instance with the provided error_message.

        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message # Displaying Error Message


# TESTING

if __name__ == "__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e, sys)








