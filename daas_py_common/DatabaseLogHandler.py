import logging
import psycopg2 
from daas_py_config import config
configs = config.get_configs()

class DatabaseLogHandler(logging.Handler):
    def __init__(self, db_config):
        super().__init__()
        self.db_config = db_config

    def emit(self, record):
        try:
            conn = psycopg2.connect(**self.db_config)
            cursor = conn.cursor()
            
            level = record.levelname
            message = self.format(record)
            file_name = record.pathname
            line_number = record.lineno

            call_statement = f"CALL {configs.DB_FUNC_LOG}(%s, %s, %s, %s)"
            params = (level, message, file_name, line_number)
            # Execute the procedure
            cursor.execute(call_statement, params)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Logging to DB failed: {e}")  # Fallback logging
