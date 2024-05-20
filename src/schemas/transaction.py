from fastapi import FastAPI
from pydantic import BaseModel , Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

class Transaction(BaseModel):
    date: datetime = Field(..., description="The date of the transaction")
    description: str = Field(..., min_length=3, max_length=50, description="The description of the transaction")
    worth: float = Field(..., gt=0, description="The worth of the transaction")
    category: str = Field(..., description="The category of the transaction")
    owner_id: Optional[int] = Field(None, description="The ID of the owner")

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
        orm_mode = True
        json_schema_extra = {
            "example": {
                "date": "2024-03-04",
                "description": "Salary",
                "worth": 500000,
                "category": "Salary",
                "owner_id": 1
            }
        }
        
