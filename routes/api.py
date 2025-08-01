from fastapi import APIRouter
from src.endpoints import books, users, addresses

from fastapi import FastAPI

app = FastAPI(

    title="01-08-2025 - Python FastApi and MongoDB at Atlas",
    description="FastAPI serving CRUD towards MongoDB Atlas",
    version="0.0.1",
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
        
        },
)


router = APIRouter()

app.include_router(router)

router.include_router(books.router)
router.include_router(users.router)
router.include_router(addresses.router)


