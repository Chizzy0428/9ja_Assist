import streamlit as st

# Retrieve keys from Streamlit secrets
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")
TAVILY_API_KEY = st.secrets.get("TAVILY_API_KEY")
