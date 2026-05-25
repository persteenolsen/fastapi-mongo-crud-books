from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.users import User
from bson import ObjectId

# This file contains the logic for handling the users collection in the MongoDB database, 
# including creating, listing, finding and deleting users.
def get_collection_users(request: Request):
    return request.app.database["users"]

def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = get_collection_users(request).insert_one(user)
    created_user = get_collection_users(request).find_one({"_id": new_user.inserted_id})
    return created_user

# Note: Added a new Model UserList to display the user id for deleting
def list_users(request: Request, limit: int):
    users = get_collection_users(request).find().limit(limit)

    return [
        {
            "user_id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
        for user in users
    ]


def find_user(request: Request, id: str):
    if (user := get_collection_users(request).find_one({"_id": ObjectId(id)})):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")


def delete_user(request: Request, id: str):
    deleted_user = get_collection_users(request).delete_one({"_id": ObjectId(id)})

    if deleted_user.deleted_count == 1:
        return f"User with id {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")