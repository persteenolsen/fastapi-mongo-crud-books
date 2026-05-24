from fastapi import APIRouter, Body, Request, status, Depends
from typing import List
from src.models.users import User, UserList

import src.rules.users as users

from auth.dependencies import get_current_user

router = APIRouter(prefix="/user",
    tags=["User"])

# Public routes for List and Get operations
# Note: Added a new Model UserList to display the user id for deleting
@router.get("/", response_description="List users", response_model=List[UserList])
def list_users(request: Request):
    return users.list_users(request, 100)

@router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(request: Request, id: str):    
    return users.find_user(request, id)

# Protected routes for Create and Delete operations
@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...), username: str = Depends(get_current_user)):  
    return users.create_user(request, user)

@router.delete("/{id}", response_description="Delete a user")
def delete_user(request: Request, id:str, username: str = Depends(get_current_user)):
    return users.delete_user(request, id)



