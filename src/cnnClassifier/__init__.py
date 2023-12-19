#INITIALIZATION FILE
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #SPECIFIES THE LOG MESSAGE FORMAT

#LOG DIRECTORY SETUP
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#LOGGING CONFIGURATION
logging.basicConfig(
    level=logging.INFO, #SETS THE LOGGING MESSAGE TO INFO
    format=logging_str, 

    handlers =[
        logging.FileHandler(log_filepath), #WRITE LOG MESSAGES TO SPECIFIED FILE
        logging.StreamHandler(sys.stdout) #WRITE LOG MESSAGES TO THE CONSOLE
    ]
)

logger = logging.getLogger("cnnClassifierLogger")