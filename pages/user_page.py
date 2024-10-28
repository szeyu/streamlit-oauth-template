import streamlit as st
from frames.header import header
from utils.back_to_login import back_to_login

def user_page():
    header()
    back_to_login()
    st.title("User Page")
    
    if st.button("page1"):
        st.session_state["pages"] = "page1"
        st.rerun()