import streamlit as st

def back_to_login():
    if st.button("Logout"):
        # reset the session state to go
        st.session_state["pages"] = "login"
        st.session_state["signed_in"] = False
        
        # clear the oauth uri details
        st.markdown('<meta http-equiv="refresh" content="0; url=/" />', unsafe_allow_html=True)
        
        st.rerun()