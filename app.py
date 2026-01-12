import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Your Travel & Tourism App",
    layout="wide"
)

# Read HTML file
with open('travel_tourism.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Display HTML content
st.components.v1.html(html_content, height=800, scrolling=True)
