from datetime import datetime
from typing import List

from app.data.database import database
from app.data.models.user import User, UserCreate


GET_USER_BY_EMAIL_QUERY = "SELECT * FROM users WHERE email=:email"
GET_USER_QUERY = "SELECT * FROM users WHERE id=:uid"
GET_ALL_USERS_QUERY = "SELECT * FROM users"


class UserQuery:
    def __init__(self, db=database):
        self.db = db

    async def get_by_email(self, email: str) -> User:
        result = await self.db.fetch_one(
            GET_USER_BY_EMAIL_QUERY, {"email": email}
        )
        if result:
            return User(**result)
        else:
            raise Exception(f"Not found user with email: {email}")

    async def get(
        self,
        uid: int,
    ) -> User:
        result = await self.db.fetch_one(GET_USER_QUERY, {"uid": uid})
        if result:
            return User(**result)
        else:
            raise Exception(f"Not found user with email: {uid}")

    async def get_all(self) -> List[User]:
        result = await self.db.fetch_all(GET_ALL_USERS_QUERY)
        return [User(**user) for user in result]

    async def create(self, user: UserCreate) -> None:
        try:
            await database.execute(
                "INSERT INTO users (username, email, password_hash, created_at) "
                "VALUES ('%s', '%s', '%s', '%s');"
                % (
                    user.username,
                    user.email,
                    user.password_hash,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
            )
        except Exception as e:
            raise e


user_query = UserQuery()
