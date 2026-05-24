import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from dotenv import load_dotenv

from auth.jwt_service import jwt_service

load_dotenv()

router = APIRouter()

USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "password")

# Used by Swagger UI to get the token
@router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):

    if form.username != USERNAME or form.password != PASSWORD:
        raise HTTPException(
            status_code=401,
            detail="Bad credentials"
        )

    token = jwt_service.create_token(form.username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }