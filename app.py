import streamlit as st
from utils.init_session import init_session
from pages.login import login
from pages.page1 import page1
from pages.user_page import user_page

def main():  
    init_session()
    
    # A container for the main content
    main_container = st.container()
    with main_container:
        if st.session_state['signed_in']:
            if st.session_state['pages'] == "user_page":
                user_page()
            
            if st.session_state['pages'] == 'page1':
                page1()

        else:
            if st.session_state['pages'] == 'login':
                login()    
    
if __name__ == "__main__":
    main()
