import json
from typing import Annotated

from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from app.data.models.token import Token
from app.data.models.user import UserCredentials, User, UserCreate
from app.data.models import DateTimeEncoder

from app.routes.dependences.authorization import (
    Unauthorized,
    authorization_handler,
)
from app.services.authorization_service import AuthException
from app.services.user_service import (
    user_service,
    UserServiceException,
)

user_router = APIRouter(
    prefix="/account",
    tags=["account"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@user_router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    response: Response,
):
    try:
        user = await authorization_handler.authenticate_user(
            UserCredentials(
                email=form_data.username, password=form_data.password
            )
        )
    except (AuthException, UserServiceException):
        raise

    access_token = await authorization_handler.authorize_user(user, response)
    return access_token


@user_router.get("/me", response_model=User)
async def read_users_me(
    claims: Annotated[
        User, Depends(authorization_handler.validate_access_token)
    ]
):
    try:
        _user = await user_service.get(claims.id)
    except UserServiceException:
        raise Unauthorized("Who are you? Please reauthenticate to the system")

    return User(**_user.dict())


@user_router.get("/refresh", response_model=Token)
async def refresh_tokens(
    claims: Annotated[
        User, Depends(authorization_handler.validate_refresh_token)
    ],
    response: Response,
):
    try:
        user = await user_service.get(claims.id)
    except UserServiceException:
        raise Unauthorized("Who are you? Please reauthenticate to the system")

    user = User(
        email=user.email,
        username=user.username,
        id=user.id,
    )
    access_token = await authorization_handler.authorize_user(user, response)
    return access_token


@user_router.post("/register/", response_model=Token)
async def create_new_user(user: UserCreate, response: Response):
    try:
        await user_service.create_user(user)
    except UserServiceException as e:
        raise HTTPException(status_code=500, detail=e)

    try:
        user = await authorization_handler.authenticate_user(
            UserCredentials(email=user.email, password=user.password)
        )
    except (AuthException, UserServiceException):
        raise

    access_token = await authorization_handler.authorize_user(user, response)
    return access_token


@user_router.get("/users/{user_id}", response_model=User)
async def get_single_user(user_id: int):
    user = await user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return JSONResponse(
        status_code=200,
        content={"user": json.dumps(dict(user), cls=DateTimeEncoder)},
    )


@user_router.get("/users/")
async def get_all_user():
    res = await user_service.get_all_users()
    users = json.dumps(res, cls=DateTimeEncoder)
    return JSONResponse(status_code=200, content={"users": users})
