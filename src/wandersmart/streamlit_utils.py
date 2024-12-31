import os
import logging
import json
from logging.handlers import RotatingFileHandler
from crew import Wandersmart  # Importing the CrewAI instance
from dotenv import load_dotenv

load_dotenv()

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
    os.makedirs(logs_dir, exist_ok=True)  # Create logs directory if it doesn't exist
    file_handler = RotatingFileHandler(
        os.path.join(logs_dir, 'streamlit_utility.log'),
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3  # Keep last 3 log files
    )
    file_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)

# Test logging function
def test_logging():
    logger.debug("Debugging information for developers.")
    logger.info("General information for development.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical issue!")

# Fetch itinerary function
from crew import Wandersmart

def fetch_itinerary(user_inputs):
    logger.debug(f"User inputs: {user_inputs}")
    crew = Wandersmart().crew()
    raw_response = crew.kickoff(inputs=user_inputs)
    logger.debug(f"Raw response: {raw_response}")
    
    # Ensure raw_response is a dictionary
    if hasattr(raw_response, "dict"):
        raw_response = raw_response.dict()
    elif isinstance(raw_response, str):
        # Remove leading ```json and trailing ```
        raw_response = raw_response.strip("```json").strip("```")
        raw_response = json.loads(raw_response)
    
    # Extract and print only the "raw" keys and values
    raw_values = extract_raw_values(raw_response)
    logger.debug(f"Extracted raw values: {raw_values}")
    
    return raw_values

def extract_raw_values(json_data):
    """
    Extract values associated with the "raw" keys from the JSON data.

    Args:
        json_data (dict): The JSON data to parse.

    Returns:
        dict: A dictionary of "raw" keys and their associated values.
    """
    raw_values = {}

    def recursive_extract(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "raw":
                    raw_values[key] = value
                else:
                    recursive_extract(value)
        elif isinstance(data, list):
            for item in data:
                recursive_extract(item)

    recursive_extract(json_data)
    return raw_values

if __name__ == "__main__":
    test_logging()  # Keep this for logging tests
    
    # Test fetch_itinerary
    test_inputs = {
        "destination": "Paris",
        "budget": 2000,
        "start_date": "2024-01-01",
        "end_date": "2024-01-10",
        "interests": ["Art", "History"]
    }
    results = fetch_itinerary(test_inputs)
    print(results)
