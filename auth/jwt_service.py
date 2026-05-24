import os
from datetime import datetime, timedelta

from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()

class JWTService:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY", "dev-secret")
        self.algorithm = os.getenv("ALGORITHM", "HS256")
        self.expire_minutes = 30
        if not self.secret_key:
            raise ValueError("SECRET_KEY missing")

    def create_token(self, username: str):
        payload = {
            "sub": username,
            "exp": datetime.utcnow() + timedelta(minutes=self.expire_minutes)
        }

        return jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm
        )

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )

            return payload.get("sub")

        except JWTError:
            return None


jwt_service = JWTService()