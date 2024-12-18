import streamlit as st

# Basic setup for the Streamlit app
st.set_page_config(page_title="WanderSmart", layout="wide")

# App Header
st.title("WanderSmart")
st.subheader("Your AI-powered travel companion for European adventures")
st.write("Plan your dream European trip effortlessly with smart, tailored recommendations.")

# Sidebar for Navigation
with st.sidebar:
    st.header("Explore WanderSmart")
    page = st.radio("Navigate to:", ["Home", "Destination Explorer", "Trip Planner", "Chat with AI", "Feedback"])

# Home Page
if page == "Home":
    st.image("./pexels-pixabay-269790.jpg", caption="Explore Europe like never before with WanderSmart.", use_container_width=True)
    st.write("\n")
    st.write("WanderSmart combines cutting-edge AI with personalized travel planning. Use our tools to discover amazing destinations, create tailored itineraries, and chat with AI agents for real-time assistance.")

# Destination Explorer Page
elif page == "Destination Explorer":
    st.header("Explore Popular European Destinations")
    st.write("Discover top destinations, handpicked for you.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./paris.png", caption="Paris", width=100)
        st.button("Learn More", key="paris")
    with col2:
        st.image("./rome.png", caption="Rome", width=100)
        st.button("Learn More", key="rome")
    with col3:
        st.image("./barcelona.png", caption="Barcelona", width=100)
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

    if st.button("Get My Itinerary"):
        st.write(f"Thank you, {name}! Your itinerary will be based on:")
        st.write(f"Dates: {start_date} to {end_date}")
        st.write(f"Budget: ${budget}")
        st.write(f"Interests: {', '.join(interests) if interests else 'None specified'}")
        st.write("[AI-generated itinerary coming soon]")

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
