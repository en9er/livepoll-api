from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime| None = None


class UserDB(User):
    password_hash: str


class UserCredentials(BaseModel):
    email: str
    password_hash: str
