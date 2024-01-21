"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Aldrin&Ramagopal''')
    st.image("./images/icon.jpg")
    st.markdown('''### https://github.com/Krishnanramagopal191/Health_RX''')
    