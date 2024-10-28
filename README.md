# streamlit-oauth-template

A Streamlit template that handles login using OAuth and manages navigation between login and app states.

## How to Use

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OAuth provider credentials (e.g., Google, GitHub)

### Installation

1. Fork the repository on GitHub.
2. Clone your forked repository:
    ```bash
    git clone https://github.com/yourusername/streamlit-oauth-template.git
    ```
3. Navigate to the project directory:
    ```bash
    cd streamlit-oauth-template
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory and add your OAuth provider credentials:
    ```env
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    GOOGLE_REDIRECT_URI=http://localhost:8501
    GOOGLE_SCOPE=https://www.googleapis.com/oauth2/v1/certs
    GOOGLE_HOSTED_DOMAIN=your_customer_email_hosted_domain
    ```

### Running the App

1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your browser and navigate to `http://localhost:8501`.

### Customization

- Modify `app.py` to customize the app's behavior.
- Modify `frames/header.py` to customize the app's description.
- Add more `<page>.py` files to add more functionality to the app.
- Update `oauth.py` to change OAuth provider settings.

### Troubleshooting

- Ensure your OAuth credentials are correct.
- Check the Streamlit logs for any errors.

## License

This project is licensed under the [MIT License](LICENSE).
