import streamlit as st

def back_to_home():
    if st.button("Back to Home"):
        st.session_state["pages"] = "user_page"
        st.rerun()