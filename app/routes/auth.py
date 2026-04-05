from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.utils.auth import getGoogleFlow

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
def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Missing code or state")

    flow.fetch_token(code=code)
    credentials = flow.credentials
    return {
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_expiry": credentials.expiry.isoformat()
    }