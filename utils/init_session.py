import streamlit as st

def init_session():
    # Check if the user is signed in
    if "signed_in" not in st.session_state:
        st.session_state["signed_in"] = False
    
    if "pages" not in st.session_state:
        st.session_state["pages"] = "login"