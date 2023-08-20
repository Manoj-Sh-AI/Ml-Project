# This script is used to record all the execution logs occured in the project

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # its a text file in this naming convention
                                                                 # # %m = month, %d= day, %Y = year, %H = hour, %M = minuts, %S = seconds

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # getcwd() -> current working directory AND all log files will be creared in current working directoy
os.makedirs(logs_path, exist_ok=True)  # Keeps on appending the files even though if there is a folder

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# over writing logging functionality
logging.basicConfig(
    filename=LOG_FILE_PATH, # which pile path thee file should be saved
    format="[ %(asctime)s ] %(lineno)d %(name)s %(levelname)s - %(message)s", # convention/naming format for how logging message will be printed
    level=logging.INFO, # in case of INFO, the logging message will be printed
)

# TESTING
# if __name__ == "__main__":
#     logging.info("Logging has started")






