from pydantic import BaseModel, EmailStr
from typing import List, Optional
from src.schemas.transaction import Transaction

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True
