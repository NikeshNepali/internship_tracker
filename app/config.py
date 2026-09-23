# For database.
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


database = {
    "env": os.getenv("ENV"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "name": os.getenv("DB_NAME")
}

# For Google OAuTH
google_oauth = {
    "client_secret_file": os.getenv("GOOGLE_CLIENT_SECRET_FILE"),
    "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI"),
    "scopes": os.getenv("GOOGLE_SCOPES", "openid email profile").split(",")
}

jwt_config = {
    "secret_key": os.getenv("SECRET_KEY"),
    "algorithm": os.getenv("ALGORITHM"),
    "access_token_expire_minutes": int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)),
    "refresh_token_expire_days": int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))
}