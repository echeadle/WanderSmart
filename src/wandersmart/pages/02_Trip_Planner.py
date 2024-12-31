import streamlit as st
from crew import Wandersmart
from streamlit_utils import fetch_itinerary, extract_raw_values

st.header("Plan Your Trip")
st.write("Answer a few questions to help us tailor your perfect European adventure.")

# User inputs
name = st.text_input("What is your name?")
destination = st.text_input("Where do you want to go?")
start_date = st.date_input("When do you want to start your trip?")
end_date = st.date_input("When do you want to return?")
budget = st.slider("What is your budget (in $)?", 500, 10000, step=500)
interests = st.multiselect(
    "What are you interested in?",
    ["History", "Art", "Food", "Nightlife", "Nature", "Shopping"]
)

# Validate inputs
if start_date > end_date:
    st.error("Error: Start date must be before the end date.")
elif st.button("Get My Itinerary"):
    # Prepare inputs for fetch_itinerary
    user_inputs = {
        "destination": destination,
        "budget": budget,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "interests": interests
    }
    
    # Debug: Log user inputs
    st.write(f"User inputs: {user_inputs}")
    
    # Fetch itinerary
    results = fetch_itinerary(user_inputs)

    # Display the "raw" keys and values
    raw_values = extract_raw_values(results)
    st.json(raw_values)
