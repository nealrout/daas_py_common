import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
logger = logging.getLogger('daas_py')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
file_handler = RotatingFileHandler(
    'app.log',  # Log file name
    maxBytes=5 * 1024 * 1024,  # Maximum file size (5 MB)
    backupCount=3  # Number of backup files to keep
)

# Create a console handler
console_handler = logging.StreamHandler()

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the formatter for both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
