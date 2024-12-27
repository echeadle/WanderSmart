import logging  # Required for updating logger handlers
import streamlit as st
from dotenv import load_dotenv
import os

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
