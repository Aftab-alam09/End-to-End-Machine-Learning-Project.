import sys
def error_messege_detail(error,error_detail:sys):
    # error is the error which we are getting in our code and 
    # we are passing it to this function and we are also passing the error_detail which is the sys module.
    # error_detail is the sys module which will give us the details of the error.
    
    _,_,exc_tb = error_detail.exc_info()
# exc_info() is a function which will give us the details of the error and it will return a tuple of three values,
    # the first value is the type of the error, 
    # the second value is the value of the error and the third value is the traceback of the error.

    file_name = exc_tb.tb_frame.f_code.co_filename
    # tb_frame is the frame object which will give us the details of the frame and 
    # f_code is the code object which will give us the details of the code and 
    # co_filename is the name of the file which is giving us the error.
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message
# we are creating a custom exception class which will inherit from the Exception class and
#  we are overriding the __init__ method and we are also overriding the __str__ method to return the error message.

class CustomException(Exception):
# we are creating a custom exception class which will inherit from the Exception class and
#  we are overriding the __init__ method and we are also overriding the __str__
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_messege_detail(error_message,error_detail=error_detail)
# we are creating a custom exception class which will inherit from the Exception class and
#  we are overriding the __init__ method and we are also overriding the __str__ method to return the error message.
    def __str__(self):
        return self.error_message



