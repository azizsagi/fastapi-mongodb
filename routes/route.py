from fastapi import FastAPI
from fastapi import APIRouter
from models.user_model import User
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET Method
@router.get("/")
async def get_users():
    users = list_serial(collection_name.find())
    return users

# Post Method
@router.post("/")
async def add_users(user: User):
    collection_name.insert_one(dict(user))


# Update Method
@router.put("/{id}")
async def update_users(id:str, user:User):
    collection_name.find_one_and_update({"_id": ObjectId(id) },{"$set" : dict(user)})

# Delete Method
@router.delete("/{id}")
async def delete_user(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)}) 