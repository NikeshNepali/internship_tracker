from app.models.User import User
from sqlalchemy.orm import Session
from app.models.refresh import RefreshToken
from app.utils.jwt import create_access_token, create_refresh_token

def get_or_create_user(db: Session, google_user: dict, google_refresh_token: str = None):
    user = db.query(User).filter(User.google_id == google_user["id"]).first()
    if user:
        return user
    
    new_user = User(
        google_id=google_user["id"],
        email=google_user["email"],
        name=google_user["name"],
        google_refresh_token=google_refresh_token,
        app_refresh_token=create_refresh_token({"user_id": google_user["id"], "email": google_user["email"]})
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

