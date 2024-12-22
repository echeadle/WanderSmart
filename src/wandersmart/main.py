import logging
import os
import sys
import json
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from crew import crew

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


# Load environment variables
load_dotenv()

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(SCRIPT_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

# Configuration for logging handlers
ENABLE_CONSOLE_LOGGING = os.getenv('ENABLE_CONSOLE_LOGGING', 'true').lower() == 'true'
ENABLE_FILE_LOGGING = os.getenv('ENABLE_FILE_LOGGING', 'true').lower() == 'true'

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# JSON formatter for structured logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)

json_formatter = JSONFormatter()

# Handlers
if ENABLE_CONSOLE_LOGGING:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

if ENABLE_FILE_LOGGING:
    file_handler = RotatingFileHandler(
        os.path.join(LOGS_DIR, 'wandersmart.log'),
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3  # Keep last 3 log files
    )
    file_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)

# Test logging configuration
logger.debug("Logging configuration completed. Console Logging: "
             f"{ENABLE_CONSOLE_LOGGING}, File Logging: {ENABLE_FILE_LOGGING}")

if __name__ == "__main__":
    logger.info("Logging system initialized.")
    
    # Define test inputs
    inputs = {"destination": "Paris"}
    logger.info(f"Starting minimal CrewAI execution with inputs: {inputs}")
    
    try:
        # Run the crew
        results = crew.kickoff(inputs=inputs)
        logger.info("Execution completed.")
        logger.info(f"Results: {results}")
    except Exception as e:
        logger.error(f"Error during CrewAI execution: {e}", exc_info=True)
