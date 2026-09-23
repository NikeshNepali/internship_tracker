from jose import jwt
from datetime import datetime, timedelta
from app.config import jwt_config

secret_key = jwt_config["secret_key"]
algorithm = jwt_config["algorithm"]
access_token_expire_minutes = jwt_config["access_token_expire_minutes"]
refresh_token_expire_days = jwt_config["refresh_token_expire_days"]

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=refresh_token_expire_days)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)
