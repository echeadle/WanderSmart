import os
import streamlit as st
from dotenv import load_dotenv, set_key

load_dotenv()

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
    set_key('.env', 'ENABLE_CONSOLE_LOGGING', 'true' if enable_console else 'false')
    set_key('.env', 'ENABLE_FILE_LOGGING', 'true' if enable_file else 'false')
    st.success("Logging settings updated! Please restart the application for changes to take effect.")
