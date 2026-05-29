from jose import jwt
from datetime import datetime, timedelta
from app.config import jwt_config

secret_key = jwt_config["secret_key"]
algorithm = jwt_config["algorithm"]
access_token_expire_minutes = jwt_config["access_token_expire_minutes"]
refresh_token_expire_days = jwt_config["refresh_token_expire_days"]

