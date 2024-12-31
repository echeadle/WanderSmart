import logging  # Required for updating logger handlers
import streamlit as st
from dotenv import load_dotenv
import os
import json

from streamlit_utils import logger, JSONFormatter  # Import logger and formatter

def update_env_file(new_settings):
    """
    Update the .env file while preserving existing keys.

    Args:
        new_settings (dict): Dictionary of settings to update in the .env file.
    """
    env_file_path = ".env"
    env_vars = {}

    # Read existing .env variables
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as file:
            for line in file:
                key, _, value = line.strip().partition("=")
                env_vars[key] = value

    # Update with new settings
    env_vars.update(new_settings)

    # Write updated variables back to .env
    with open(env_file_path, "w") as file:
        for key, value in env_vars.items():
            file.write(f"{key}={value}\n")

def update_logging():
    """
    Dynamically update logging configuration.
    """
    load_dotenv()  # Reload the updated .env file
    ENABLE_CONSOLE_LOGGING = os.getenv('ENABLE_CONSOLE_LOGGING', 'true').lower() == 'true'
    ENABLE_FILE_LOGGING = os.getenv('ENABLE_FILE_LOGGING', 'true').lower() == 'true'

    # Clear existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Reconfigure logger
    json_formatter = JSONFormatter()
    if ENABLE_CONSOLE_LOGGING:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(json_formatter)
        logger.addHandler(console_handler)

    if ENABLE_FILE_LOGGING:
        logs_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        file_handler = logging.handlers.RotatingFileHandler(
            os.path.join(logs_dir, 'streamlit_utility.log'),
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=3
        )
        file_handler.setFormatter(json_formatter)
        logger.addHandler(file_handler)

def extract_raw_values(json_data):
    """
    Extract values associated with the "raw" keys from the JSON data.

    Args:
        json_data (dict): The JSON data to parse.

    Returns:
        list: A list of values associated with the "raw" keys.
    """
    raw_values = []

    def recursive_extract(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "raw":
                    raw_values.append(value)
                else:
                    recursive_extract(value)
        elif isinstance(data, list):
            for item in data:
                recursive_extract(item)

    recursive_extract(json_data)
    return raw_values

# Logging Control UI
st.header("Logging Settings")

enable_console = st.checkbox(
    "Enable Console Logging", 
    value=os.getenv('ENABLE_CONSOLE_LOGGING', 'false').lower() == 'true'
)
enable_file = st.checkbox(
    "Enable File Logging", 
    value=os.getenv('ENABLE_FILE_LOGGING', 'false').lower() == 'true'
)

if st.button("Apply Logging Settings"):
    # Update only the logging-related settings in .env
    new_settings = {
        "ENABLE_CONSOLE_LOGGING": "true" if enable_console else "false",
        "ENABLE_FILE_LOGGING": "true" if enable_file else "false"
    }
    update_env_file(new_settings)

    # Dynamically update logging configuration
    update_logging()
    st.success("Logging settings applied dynamically!")

st.header("Logging Control")
st.write("Upload a JSON log file to extract 'raw' values.")

uploaded_file = st.file_uploader("Choose a JSON log file", type="json")

if uploaded_file is not None:
    try:
        log_data = uploaded_file.read().decode("utf-8")
        if not log_data.strip():
            raise ValueError("The uploaded file is empty.")
        json_data = json.loads(log_data)
        raw_values = extract_raw_values(json_data)
        st.header("Extracted Raw Values")
        for raw_value in raw_values:
            st.json(raw_value)
    except json.JSONDecodeError as e:
        st.error(f"The uploaded file is not a valid JSON file. Error: {e}")
        logger.error(f"JSONDecodeError: {e}")
    except ValueError as e:
        st.error(f"Error: {e}")
        logger.error(f"ValueError: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        logger.error(f"Unexpected error: {e}", exc_info=True)
