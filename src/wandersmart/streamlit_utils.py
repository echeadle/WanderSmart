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
def fetch_itinerary(inputs):
    """
    Fetch an itinerary based on user inputs using CrewAI.

    Args:
        inputs (dict): A dictionary containing user inputs such as destination, budget, and interests.

    Returns:
        dict: A dictionary with matched recommendations or a message if no matches are found.
    """
    logger.info(f"Fetching itinerary with inputs: {inputs}")

    try:
        # Simulate calling CrewAI to get recommendations
        # Replace this with the actual CrewAI response
        response = {
            "destinations": [
                {
                    "location": "Bali, Indonesia",
                    "budget": "Under $1000",
                    "interests": ["Beach", "Culture", "Adventure"],
                    "attractions": ["Ubud Monkey Forest", "Tegallalang Rice Terrace", "Bali Beaches"],
                    "accommodations": ["Affordable guesthouses", "Bali villas"],
                    "transportation": "Local taxis, scooter rentals"
                },
                {
                    "location": "Rome, Italy",
                    "budget": "Under $1000",
                    "interests": ["Historical Landmarks", "Culture"],
                    "attractions": ["Colosseum", "Vatican City", "Pantheon"],
                    "accommodations": ["Budget hotels", "Hostels"],
                    "transportation": "Public transportation, walking"
                }
            ]
        }

        # Extract the destinations
        destinations = response.get("destinations", [])

        # Filter destinations based on user inputs
        matched_destinations = [
            {
                **destination,
                "title": f"{destination['location']} - {destination['budget']}"
            }
            for destination in destinations
            if inputs["destination"].lower() in destination["location"].lower()
            or set(inputs["interests"]).intersection(destination["interests"])
        ]

        if not matched_destinations:
            logger.warning("No matching recommendations found for the given inputs.")
            return {"message": "No matching recommendations found. Please adjust your preferences."}

        logger.info(f"Matched recommendations: {matched_destinations}")
        return {"recommendations": matched_destinations}

    except Exception as e:
        # Log the exception with stack trace
        logger.error(f"Error while fetching itinerary: {e}", exc_info=True)
        return {"error": "An unexpected error occurred. Please try again later."}

# def fetch_itinerary(inputs):
#     """
#     Fetch an itinerary based on user inputs using CrewAI.

#     Args:
#         inputs (dict): A dictionary containing user inputs such as destination, budget, and dates.

#     Returns:
#         dict: A dictionary representing the itinerary or an error message if something goes wrong.
#     """
#    # logger.info(f"Fetching itinerary with inputs: {inputs}")

#     results = Wandersmart().crew().kickoff(inputs=inputs)
    # return results
    # try:
    #     # Simulate calling CrewAI to get recommendations
    #     results = Wandersmart().crew().kickoff(inputs=inputs)  # Assuming crew is already imported and set up

    #     if not results:
    #         logger.warning("No itinerary returned from CrewAI.")
    #         return {"error": "No itinerary could be generated. Please try again later."}

    #     logger.info(f"Successfully fetched itinerary: {results}")
    #     return results

    # except Exception as e:
    #     # Log the exception with stack trace
    #     logger.error(f"Error while fetching itinerary: {e}", exc_info=True)
    #     return {"error": "An unexpected error occurred. Please try again later."}

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
    print(fetch_itinerary(test_inputs))
