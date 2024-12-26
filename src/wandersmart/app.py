import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="WanderSmart", layout="wide")

# Sidebar for Navigation
with st.sidebar:
    st.header("Explore WanderSmart")
    page = st.radio("Navigate to:", [
        "Home"
    ])

if page == "Home":
    st.title("Home")
    st.subheader("Your AI-powered travel companion")
    st.write("Plan your dream vacation effortlessly with smart, tailored recommendations.")
