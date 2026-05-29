from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests
from app.config import google_oauth

def getGoogleFlow():
    return Flow.from_client_secrets_file(
        google_oauth["client_secret_file"],
        scopes = google_oauth["scopes"],
        redirect_uri=google_oauth["redirect_uri"]
    )
# This function verifies the google token and returns the user information.
def verifyGoogleToken(token: str, client_id: str):
    id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)
    return id_info 