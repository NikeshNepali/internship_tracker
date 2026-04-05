from google_auth_oauthlib.flow import Flow

def getGoogleFlow():
    return Flow.from_client_secrets_file(
        'app/configuration.json',
        scopes=['https://www.googleapis.com/auth/gmail.readonly'],
        redirect_uri='http://localhost:8000/auth/callback'
    )