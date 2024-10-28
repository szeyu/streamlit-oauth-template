from oauth.auth import sign_in_button
import streamlit as st

#Sign-in Page
def sign_in():

    if "code" not in st.session_state:
        # Call Sign-in button
        sign_in_button()