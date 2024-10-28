import streamlit as st
from frames.header import header
from oauth.auth import *
from oauth.sign_in import sign_in

def login():
    header()
    
    # Call sign-in page
    sign_in()