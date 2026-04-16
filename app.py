import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="IGCSE Revision Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default chrome so the site feels standalone
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load the HTML file
html_file = os.path.join(os.path.dirname(__file__), "index.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the full HTML app inside Streamlit
# height is set tall enough to show the full page; scrolling is handled inside
components.html(html_content, height=4000, scrolling=True)
