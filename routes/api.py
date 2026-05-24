from fastapi import APIRouter
from src.endpoints import auth_routes, books, protected_routes, users, addresses

router = APIRouter()

router.include_router(books.router)
router.include_router(users.router)
router.include_router(addresses.router)

# Protected routes
router.include_router(protected_routes.router)

# Auth routes
router.include_router(auth_routes.router)


