if page == "Trip Planner":
    st.header("Plan Your Trip")
    
    name = st.text_input("What is your name?")
    start_date = st.date_input("When do you want to start your trip?")
    end_date = st.date_input("When do you want to return?")
    budget = st.slider("What is your budget (in $)?", 500, 10000, step=500)
    interests = st.multiselect(
        "What are you interested in?", 
        ["History", "Art", "Food", "Nightlife", "Nature", "Shopping"]
    )

    if st.button("Submit"):
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
