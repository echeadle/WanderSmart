import streamlit as st 

# Destination Explorer Page

st.header("Explore Popular European Destinations")
st.write("Discover top destinations, handpicked for you.")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("./images/paris1.png", caption="Paris", width=100)
    st.button("Learn More", key="paris")
with col2:
    st.image("./images/rome1.png", caption="Rome", width=100)
    st.button("Learn More", key="rome")
with col3:
    st.image("./images/barcelona.png", caption="Barcelona", width=100)
    st.button("Learn More", key="barcelona")
