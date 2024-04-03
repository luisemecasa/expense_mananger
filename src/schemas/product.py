from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the product")
    name: str = Field(min_length=4, max_length=50, title="Name of the product")
    price: float = Field(default="1000", le=5000000, lg=100, title="Price of the product")
    expiration: Optional[str] = Field(default=None, title="Expiration date of the product")

    ## Advanced field validator
    @validator("name")
    @classmethod
    def validate_no_poison(cls, value):
        if value == "poison":
            raise ValueError("Posion should not be expended as product")
        return value

    ## Advanced multi-field validator
    @model_validator(mode='after')
    def validate_expensive_cheap_products(self):
        name = self.name
        price = self.price
        if name == "cheap" and price > 100000:
            raise ValueError("A product with that price cannot be named cheap.")
        return self

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Platanitos",
                "price": 5000,
                "expiration": "2025-04-04"
            }
        }
