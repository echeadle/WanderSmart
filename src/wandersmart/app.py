import streamlit as st
import os
import sys
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Load environment variables from .env
load_dotenv()

# Function to update .env file
def update_env_file(settings):
    with open('.env', 'w') as env_file:
        for key, value in settings.items():
            env_file.write(f"{key}={value}\n")

# Set up Streamlit page
st.set_page_config(page_title="WanderSmart", layout="wide")


# Sidebar for Navigation
with st.sidebar:
    st.header("Explore WanderSmart")
    page = st.radio("Navigate to:", ["Home", "Destination Explorer", "Trip Planner", "Chat with AI", "Feedback", "Logging Control"])


# Home Page
if page == "Home":
    st.title("WanderSmart")
    st.subheader("Your AI-powered travel companion for European adventures")
    st.write("Plan your dream European trip effortlessly with smart, tailored recommendations.")
    st.image("./images/europe.jpg", caption="Explore Europe like never before with WanderSmart.", use_container_width=True)
    st.write("\n")
    st.write("WanderSmart combines cutting-edge AI with personalized travel planning. Use our tools to discover amazing destinations, create tailored itineraries, and chat with AI agents for real-time assistance.")

# Destination Explorer Page
elif page == "Destination Explorer":
    st.header("Explore Popular European Destinations")
    st.write("Discover top destinations, handpicked for you.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./images/paris.png", caption="Paris", width=100)
        st.button("Learn More", key="paris")
    with col2:
        st.image("./images/rome.png", caption="Rome", width=100)
        st.button("Learn More", key="rome")
    with col3:
        st.image("./images/barcelona.png", caption="Barcelona", width=100)
        st.button("Learn More", key="barcelona")

# Trip Planner Page
elif page == "Trip Planner":
    st.header("Plan Your Trip")
    st.write("Answer a few questions to help us tailor your perfect European adventure.")

    name = st.text_input("What is your name?")
    start_date = st.date_input("When do you want to start your trip?")
    end_date = st.date_input("When do you want to return?")
    budget = st.slider("What is your budget (in $)?", 500, 10000, step=500)
    interests = st.multiselect(
        "What are you interested in?", 
        ["History", "Art", "Food", "Nightlife", "Nature", "Shopping"]
    )

    if start_date > end_date:
        st.error("Error: Start date must be before the end date.")
    elif st.button("Submit"):
        st.write(f"Thank you, {name}! Your itinerary will be based on:")
        st.write(f"Dates: {start_date} to {end_date}")
        st.write(f"Budget: ${budget}")
        st.write(f"Interests: {', '.join(interests) if interests else 'None specified'}")
        st.write(f"If everthing above looks right, submit the itenerary.")
        # Prepare inputs for the backend
        inputs = {
                "name": name,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "budget": budget,
                "interests": interests
            }

        with st.spinner("Processing..."):
            from src.wandersmart.crew import echo_inputs  # Adjust import based on your structure
            response = echo_inputs(inputs)
            
            if "error" in response:
                st.error(f"Error: {response['error']}")
            else:
                st.success("Backend communication successful!")
                st.json(response)

# Chat with AI Page
elif page == "Chat with AI":
    st.header("Chat with Our AI Agent")
    st.write("Ask your travel questions and get instant answers.")

    user_input = st.text_input("You:", "")
    if user_input:
        st.write("[AI Response coming soon]")
        # Placeholder for Crewai API integration
        # response = crewai_chat(user_input)
        # st.write(response)

# Feedback Page
elif page == "Feedback":
    st.header("We value your feedback")
    feedback = st.text_area("How can we improve your experience?")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

elif page == "Logging Control":
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
