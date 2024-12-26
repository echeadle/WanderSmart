from dotenv import load_dotenv
import os
import streamlit as st

def update_logging():
    load_dotenv()  # Reload the .env file
    ENABLE_CONSOLE_LOGGING = os.getenv('ENABLE_CONSOLE_LOGGING', 'true').lower() == 'true'
    ENABLE_FILE_LOGGING = os.getenv('ENABLE_FILE_LOGGING', 'true').lower() == 'true'

    # Clear existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Reconfigure logger
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
    with open('.env', 'w') as env_file:
        env_file.write(f"ENABLE_CONSOLE_LOGGING={'true' if enable_console else 'false'}\n")
        env_file.write(f"ENABLE_FILE_LOGGING={'true' if enable_file else 'false'}\n")
    update_logging()
    st.success("Logging settings applied dynamically!")
