import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.models import DateTimeEncoder
from app.models.user import User, UserCreate
from app.services.user_service import create_user, get_user, get_all_users

user_router = APIRouter()


@user_router.post("/user/")
async def create_new_user(user: UserCreate):
    res, msg = await create_user(user)
    if not res:
        raise HTTPException(status_code=500, detail=msg)
    return JSONResponse(status_code=200, content={"msg": msg})


@user_router.get("/users/{user_id}", response_model=User)
async def get_single_user(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return JSONResponse(
        status_code=200, content={"user": json.dumps(dict(user), cls=DateTimeEncoder)}
    )


@user_router.get("/users/")
async def get_all_user():
    res = await get_all_users()
    users = json.dumps(res, cls=DateTimeEncoder)
    return JSONResponse(status_code=200, content={"users": users})
