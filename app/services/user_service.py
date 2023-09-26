from datetime import datetime
from typing import Optional
from app.data.models.user import User, UserCreate
from app.data.database import database
from app.data.query.user import UserQuery, user_query


class UserServiceException(Exception):
    pass


class UserService:
    query: UserQuery

    def __init__(self, query=user_query):
        self.query = query

    async def create_user(self, user: UserCreate) -> None:
        try:
            await self.query.create(user)
        except Exception as e:
            raise UserServiceException(
                f"Error occurred during creation of {user=}\n{e}"
            )

    async def get_all_users(self) -> [User]:
        return self.query.get_all()

    async def get(
        self, uid: int = None
    ) -> User:
        try:
            user =  await self.query.get(uid)
        except Exception:
            raise UserServiceException("User not found")

        return user


user_service = UserService()
