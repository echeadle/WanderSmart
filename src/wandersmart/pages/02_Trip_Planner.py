import streamlit as st
from datetime import date
from utils.constants import MIN_BUDGET, MAX_BUDGET, BUDGET_STEP, DESTINATION_INTERESTS
from utils.validation import validate_inputs
from streamlit_utils import fetch_itinerary

st.header("Trip Planner")
st.write("Plan your trip by filling in the necessary details.")

# Input Fields
name = st.text_input("What is your name?")
destination = st.text_input("Where do you want to go?")
start_date = st.date_input("When do you want to start your trip?", min_value=date.today())
end_date = st.date_input("When do you want to return?", min_value=date.today())
budget = st.slider("What is your budget (in $)?", MIN_BUDGET, MAX_BUDGET, step=BUDGET_STEP)
interests = st.multiselect("What are you interested in?", DESTINATION_INTERESTS)

if st.button("Get My Itinerary"):
    # Validate inputs
    is_valid, error_message = validate_inputs(name, destination, start_date, end_date)
    if not is_valid:
        st.error(error_message)
    else:
        # Prepare data
        inputs = {
            "name": name,
            "destination": destination,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "budget": budget,
            "interests": interests
        }

        # Call the backend utility
        with st.spinner("Fetching your itinerary..."):
            response = fetch_itinerary(inputs)
            if "error" in response:
                st.error(f"Error: {response['error']}")
            elif "recommendations" in response:
                st.success("Here is your itinerary!")
                for rec in response["recommendations"]:
                    st.markdown(f"### {rec['title']}")
                st.write(f"Price: ${rec['price']}")
                st.write(f"Details: {rec['details']}")
                st.image(rec["image"], use_container_width=True)
            else:
                st.error("No recommendations found.")
