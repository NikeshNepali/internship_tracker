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

print(f"Database configuration: {database}")