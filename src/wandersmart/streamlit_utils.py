import logging
import os
import json
from logging.handlers import RotatingFileHandler

# JSON formatter for structured logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        return json.dumps(log_record)

# Configure logger
logger = logging.getLogger("streamlit_utility")
logger.setLevel(logging.DEBUG)  # Set to DEBUG for development

# JSON formatter
json_formatter = JSONFormatter()

# Logging Handlers
ENABLE_CONSOLE_LOGGING = os.getenv('ENABLE_CONSOLE_LOGGING', 'true').lower() == 'true'
ENABLE_FILE_LOGGING = os.getenv('ENABLE_FILE_LOGGING', 'true').lower() == 'true'

if ENABLE_CONSOLE_LOGGING:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

if ENABLE_FILE_LOGGING:
    logs_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    file_handler = RotatingFileHandler(
        os.path.join(logs_dir, 'streamlit_utility.log'),
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3  # Keep last 3 log files
    )
    file_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)

# Test logger with basic logs
def test_logging():
    logger.debug("Debugging information for developers.")
    logger.info("General information for development.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical issue!")

if __name__ == "__main__":
    test_logging()
