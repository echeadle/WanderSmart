import streamlit as st 

# Feedback Page
st.header("We value your feedback")
feedback = st.text_area("How can we improve your experience?")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")