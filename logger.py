import os
import logging
from datetime import datetime

# Ensure the logs directory exists
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate a log file name based on the current timestamp
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_directory, f"blog_writing_{current_time}.log")

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler() 
f_handler = logging.FileHandler(log_file)
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
