import streamlit as st

st.header("Chat with Our AI Agent")
st.write("Ask your travel questions and get instant answers.")

user_input = st.text_input("You:", "")
if user_input:
    st.write("[AI Response coming soon]")
    # Placeholder for Crewai API integration
    # response = crewai_chat(user_input)
    # st.write(response)
