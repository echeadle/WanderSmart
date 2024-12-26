import streamlit as st 
import os

st.header("Logging Settings")

# Logging toggle controls
enable_console = st.checkbox(
    "Enable Console Logging", 
    value=os.getenv('ENABLE_CONSOLE_LOGGING', 'false').lower() == 'true'
)
enable_file = st.checkbox(
    "Enable File Logging", 
    value=os.getenv('ENABLE_FILE_LOGGING', 'false').lower() == 'true'
)

if st.button("Apply Logging Settings"):
    # Update .env with new settings
    settings = {
        'ENABLE_CONSOLE_LOGGING': 'true' if enable_console else 'false',
        'ENABLE_FILE_LOGGING': 'true' if enable_file else 'false',
    }
    update_env_file(settings)
    st.success("Logging settings updated! Please restart the application for changes to take effect.")