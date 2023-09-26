from datetime import datetime
from typing import Optional, List
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

    async def _get(
        self, uid: int = None, email: str = None
    ) -> User | List[User]:
        if uid:
            return await self.query.get(uid)
        elif email:
            return await self.query.get_by_email(email)
        else:
            return await self.query.get_all()

    async def get(self, uid: int = None, email: str = None) -> User:
        try:
            user = await self._get(uid, email)
        except Exception:
            raise UserServiceException("User not found")

        return user


user_service = UserService()
