# For database.
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


database = {
    "env": os.getenv("env"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "name": os.getenv("DB_NAME")
}
