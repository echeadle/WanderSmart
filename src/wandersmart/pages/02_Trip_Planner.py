import streamlit as st
from streamlit_utils import fetch_itinerary

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
    
    # Fetch itinerary
    results = fetch_itinerary(user_inputs)

    # Display results
    if "error" in results:
        st.error(results["error"])
    elif "message" in results:
        st.warning(results["message"])
    elif "recommendations" in results:
        st.success("Here are your recommendations:")
        for rec in results["recommendations"]:
            st.markdown(f"### {rec['title']}")
            st.write(f"**Attractions:** {', '.join(rec['attractions'])}")
            st.write(f"**Accommodations:** {', '.join(rec['accommodations'])}")
            st.write(f"**Transportation:** {rec['transportation']}")
            st.write("---")
