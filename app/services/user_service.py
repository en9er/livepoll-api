from datetime import datetime
from typing import Optional
from app.models.user import User, UserCreate
from app.data.database import database


async def create_user(user: UserCreate) -> tuple[bool, str]:
    result = False
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
        msg = str(e)
    else:
        result = True
        msg = f"User {user.username} created successfully"
    return result, msg


async def get_user(user_id: int) -> Optional[User]:
    user = await database.fetch_one("SELECT * FROM users WHERE user_id=%d" % user_id)
    return User(**user) if user else None


async def get_all_users():
    records = await database.fetch_all(
        "SELECT user_id, username, email, created_at FROM users"
    )
    users = []
    for user in records:
        users.append(dict(User(**user)))
    return users if users else []
