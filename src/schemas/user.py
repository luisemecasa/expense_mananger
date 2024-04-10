from pydantic import BaseModel
from typing import List
from src.schemas.transaction import Transaction

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True