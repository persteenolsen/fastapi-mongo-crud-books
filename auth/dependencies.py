from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_service import jwt_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = jwt_service.verify_token(token)

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return username