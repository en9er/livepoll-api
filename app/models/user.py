from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str


class User(BaseModel):
    user_id: int
    username: str
    email: str
    created_at: datetime
