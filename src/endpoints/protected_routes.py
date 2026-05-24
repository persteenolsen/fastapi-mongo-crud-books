from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user

router = APIRouter()

@router.get("/protected")
def protected_route(username: str = Depends(get_current_user)):
    return {
        "message": f"Hello {username}, protected route works."
    }
