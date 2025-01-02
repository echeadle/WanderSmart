import streamlit as st
from streamlit_utils import fetch_itinerary, convert_to_markdown, generate_markdown

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
    #st.write(f"User inputs: {user_inputs}")
    
    # Fetch itinerary
    results = fetch_itinerary(user_inputs)
  
    # Display the "raw" keys and values
    #raw_values = extract_raw_values(results)
    st.json(results)
    
    to_markdown = generate_markdown(results)
    
    markme="""
# Vacation Recommendations

## 1. Cultural Immersion in Paris
**Description:**  
Dive deep into the history and art of Paris with a package that includes a historical landmarks tour and a visit to the Louvre Museum. You'll explore Notre Dame Cathedral, Sainte-Chapelle, and marvel at thousands of art pieces, including the Mona Lisa.

**Cost:**  
- Tour Price: Starting at $150 per person  
- Total Estimate: $300 for two  

**[Learn More](https://www.tripadvisor.com/Attractions-g187147-Activities-c42-t228-Paris_Ile_de_France.html)**

---

## 2. Gastronomic Experience
**Description:**  
Enjoy guided culinary tours to taste the best of Paris’ street food and gourmet experiences. Savor traditional dishes while learning about the city's rich food culture.

**Cost:**  
- Tour Price: Starting at $120 per person  
- Total Estimate: $240 for two  

**[Learn More](https://www.eatingeurope.com/tours/paris/)**

---

## 3. Luxury at the Eiffel Tower
**Description:**  
Indulge in a unique dinner experience at the Eiffel Tower with Collette Tours, which combines fine dining with iconic views of the city. This evening will be one to remember, under the sparkling lights of Paris.

**Cost:**  
- Tour Price: $250 per person  
- Total Estimate: $500 for two  

**[Learn More](https://www.gocollette.com/en/tours/europe/france/spotlight-on-paris)**

---

"""
    
    st.markdown(markme)
    
    

