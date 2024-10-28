import streamlit as st
from frames.header import header
from utils.back_to_home import back_to_home
from utils.back_to_login import back_to_login

def page1():
    header()
    back_to_login()
    st.title("Page 1")
    back_to_home()