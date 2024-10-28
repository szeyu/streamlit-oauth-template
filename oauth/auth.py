import os
from dotenv import load_dotenv
from authlib.integrations.requests_client import OAuth2Session
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
import asyncio
import httpx

# Load Google Cloud OAuth 2.0 Client IDs
load_dotenv('.env')
CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
REDIRECT_URI = os.environ['GOOGLE_REDIRECT_URI']
HOSTED_DOMAIN = os.environ['GOOGLE_HOSTED_DOMAIN']  # This should be 'siswa.um.edu.my'


# Initialize OAuth2 client
client = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
oauth = OAuth2Session(CLIENT_ID, CLIENT_SECRET, redirect_uri=REDIRECT_URI)

# Google OAuth2 token endpoint
TOKEN_URL = "https://oauth2.googleapis.com/token"
JWKS_URL = "https://www.googleapis.com/oauth2/v3/certs"  # URL to get Google's public keys


# Exchange the code for access token and ID token
def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    # Define the token request payload
    payload = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }

    # Make the POST request to exchange the authorization code for tokens
    response = httpx.post(TOKEN_URL, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the tokens (including access token and ID token)
    elif response.status_code == 401:
        st.warning(f"Failed to obtain tokens: {response.text}")
        return None


# Generate Google OAuth authorization URL
async def get_authorization_url(client, redirect_uri, hd=HOSTED_DOMAIN):
    scopes = "openid email profile"
    base_url = 'https://accounts.google.com/o/oauth2/v2/auth'

    # Set the necessary parameters for the OAuth request
    params = {
        'response_type': 'code',
        'client_id': client.client_id,
        'redirect_uri': redirect_uri,
        'scope': scopes,
        'access_type': 'offline',
        'prompt': 'select_account',
        'hd': hd  # Restrict sign-in to the hosted domain
    }

    # Construct the full authorization URL with parameters
    query_string = '&'.join(f'{key}={value}' for key, value in params.items())
    return f'{base_url}?{query_string}'

# Check if the domain is allowed
def is_domain_allowed(email):
    domain = email.split('@')[-1]
    return domain in HOSTED_DOMAIN


# Sign-in button
def sign_in_button():
    # Generate the authorization URL
    authorization_url = asyncio.run(get_authorization_url(client, REDIRECT_URI, hd=HOSTED_DOMAIN))

    # After OAuth callback - check for authorization code
    query_params = st.query_params
    if "code" in query_params:
        # Exchange the authorization code for tokens
        code = st.query_params["code"]

        # Exchange the authorization code for tokens
        tokens = exchange_code_for_token(code, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

        if tokens:
            # Store tokens in session state
            st.session_state["access_token"] = tokens.get("access_token")
            st.session_state["id_token"] = tokens.get("id_token")

            access_token = st.session_state["access_token"]
            id_token = st.session_state["id_token"]

            # to-do: Verify and decode the ID token to get user information
            # user_info = verify_id_token(id_token)
            # if user_info:
            #     email = user_info.get("email")
            #     st.write(f"Welcome, {email}!")
            # else:
            #     st.warning("Failed to decode ID token.")

        if code:
            st.session_state["signed_in"] = True
            st.session_state["pages"] = "user_page"
            st.header("Login Successful!")
            st.rerun() # make the page go to user page
        else:
            st.warning("Failed to obtain access token.")

    # Show the login button if the user is not signed in
    if not st.session_state["signed_in"]:
        st.markdown(
            f"""
            <div style="
                display: flex; 
                justify-content: center; 
                align-items: flex-start; 
                height: 100vh;
                padding-top: 10px;">
                <div style="
                    text-align: center; 
                    background: white; 
                    padding: 40px; 
                    border-radius: 8px; 
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
                    max-width: 400px; 
                    width: 100%;">
                    <h2 style="color: #333;">Sign In</h2>
                    <a target="_self" href="{authorization_url}">
                        <button style="
                            width: 100%; 
                            padding: 12px 0; 
                            font-size: 16px; 
                            color: white; 
                            background-color: #4285F4; 
                            border: none; 
                            cursor: pointer; 
                            border-radius: 4px;
                            outline: none;">
                            Login via Siswa Mail
                        </button>
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


