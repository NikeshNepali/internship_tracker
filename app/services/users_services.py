from apps.models.User import User
from sqlalchemy.orm import Session

def get_or_create_user(db: Session, google_user: dict, google_refresh_token: str = None):
    user = db.query(User).filter(User.google_id == google_user["google_id"]).first()
    if user:
        return user
    
    new_user = User(
        google_id=google_user["google_id"],
        email=google_user["email"],
        name=google_user["name"],
        google_refresh_token=google_refresh_token)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

