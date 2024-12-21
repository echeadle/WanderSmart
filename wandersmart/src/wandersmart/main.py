import logging
from dotenv import load_dotenv
from crew import crew
import sys
import os

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(SCRIPT_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(os.path.join(LOGS_DIR, 'wandersmart.log'), mode='a')

# Create formatters and add it to handlers
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logging
logger.debug("Logging configuration completed")

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    logger.info("Logging system initialized.")
    
    # Define test inputs
    inputs = {"destination": "Paris"}
    
    logger.info("Starting minimal CrewAI execution.")
    
    try:
        # Run the crew
        results = crew.kickoff(inputs=inputs)
        logger.info("Execution completed.")
        logger.info(f"Results: {results}")
    except Exception as e:
        logger.error(f"Error during CrewAI execution: {e}", exc_info=True)
