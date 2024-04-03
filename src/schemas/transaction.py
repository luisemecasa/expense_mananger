from fastapi import FastAPI
from pydantic import BaseModel , Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import uuid4

class Transaction(BaseModel):
    id: str = Field(default_factory=uuid4, description="The id of the transaction")
    date: datetime = Field(..., description="The date of the transaction")
    description: str = Field(..., min_length=3, max_length=50, description="The description of the transaction")
    worth: float = Field(..., gt=0, description="The worth of the transaction")
    category: str = Field(..., description="The category of the transaction")

    @validator('worth')
    def worth_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('worth must be a positive number')
        return v
    
    @validator('date')
    def date_must_be_past_or_present(cls, v):
        if v > datetime.now():
            raise ValueError('date must be in the past or present')
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "id": "",
                "date": "2025-04-04",
                "description": "Salary",
                "worth": 500000,
                "category": "Salary"
            }
        }
