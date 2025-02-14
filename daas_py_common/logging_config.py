import logging
from daas_py_common.DatabaseLogHandler import DatabaseLogHandler
from logging.handlers import RotatingFileHandler
logger = logging.getLogger('daas_py')
logger.setLevel(logging.DEBUG)
from daas_py_config import config
configs = config.get_configs()

db_config = {
    'dbname': configs.DATABASE_NAME,
    'user': config.get_secret('DATABASE_USER'),
    'password': config.get_secret('DATABASE_PASSWORD'),
    'host': configs.DATABASE_HOST, 
    'port': configs.DATABASE_PORT,
    "options": f"-c search_path={configs.DATABASE_SCHEMA}"
}

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    'app.log',  # Log file name
    encoding="utf-8",
    maxBytes=5 * 1024 * 1024,  # Maximum file size (5 MB)
    backupCount=3,  # Number of backup files to keep
)
db_handler = DatabaseLogHandler(db_config)

# Set the formatter
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
db_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(db_handler)