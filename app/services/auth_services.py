from sqlalchemy.orm import Session
from app.services.users_services import get_or_create_user
from app.models.refresh import RefreshToken
from app.utils.jwt import create_access_token, create_refresh_token

def login_with_google(db: Session, google_user: dict, google_refresh_token: str = None):
    user = get_or_create_user(db, google_user, google_refresh_token)
    
    access_token = create_access_token({"user_id": user.id, "email": user.email})
    refresh_token = create_refresh_token({"user_id": user.id, "email": user.email})
    
    store_refresh_token(db, user.id, refresh_token)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user
    }

def store_refresh_token(db: Session, user_id: int, refresh_token: str):
    db_token = RefreshToken(user_id=user_id, token=refresh_token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token