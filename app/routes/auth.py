from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.utils.auth import getGoogleFlow
from app.services.users_services import get_or_create_user
from app.services.auth_services import login_with_google
from app.utils.auth import getGoogleFlow, verifyGoogleToken
from app.dependencies import get_db
from sqlalchemy.orm import Session

import requests



router = APIRouter()
flow = getGoogleFlow()


@router.get("/login")
def login():
    authorization_url, state = flow.authorization_url(
        prompt='consent',
        access_type='offline'
    )
    return RedirectResponse(authorization_url)

@router.get("/callback")
def callback(
    request: Request,
    db: Session = Depends(get_db)
):
    code = request.query_params.get("code")

    if not code:
        raise HTTPException(
            status_code=400,
            detail="Missing code or state"
        )

    # Exchange authorization code for tokens
    flow.fetch_token(code=code)

    credentials = flow.credentials
    print("Access Token:", credentials.token)  # Debugging line
    

    # Get Google user information
    google_response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={
            "Authorization": f"Bearer {credentials.token}"
        }
    )
    google_user = google_response.json()
    # Convert Google response to your format
    tokens = login_with_google(db, google_response.json(), credentials.refresh_token)

    user = get_or_create_user(db, google_user, credentials.refresh_token)

    return {
        "message": "Login successful",
        "user_id" : user.id,
        "name": user.name,
        "email": user.email
    }