from fastapi import FastAPI
from pydantic import BaseModel , Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import uuid4


tags_metadata = [
    {
        "name": "income",
        "description": "Operations with income transactions",
    },
    {
        "name": "expenses",
        "description": "Operations with expense transactions",
    },
    {
        "name": "report",
        "description": "Generate income and expense reports",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

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

income = []
expenses = []

@app.post("/income", tags=["income"])
def add_income(transaction: Transaction):
    income.append(transaction)
    return transaction

@app.get("/income", tags=["income"])
def get_income():
    return income

@app.delete("/income/{transaction_id}", tags=["income"])
def delete_income(transaction_id: str):
    global income
    income = [i for i in income if i.id != transaction_id]
    return {"message": "Transaction deleted"}

@app.post("/expenses", tags=["expenses"])
def add_expense(transaction: Transaction):
    expenses.append(transaction)
    return transaction

@app.get("/expenses", tags=["expenses"])
def get_expenses():
    return expenses

@app.delete("/expenses/{transaction_id}", tags=["expenses"])
def delete_expense(transaction_id: int):
    global expenses
    expenses = [i for i in expenses if i.id != transaction_id]
    return {"message": "Transaction deleted"}

@app.get("/report/basic", tags=["report"])
def basic_report():
    total_income = sum(i.worth for i in income)
    total_expenses = sum(e.worth for e in expenses)
    balance = total_income - total_expenses
    return {"total_income": total_income, "total_expenses": total_expenses, "balance": balance}

@app.get("/report/expanded" , tags=["report"])
def expanded_report():
    income_by_category = {}
    for i in income:
        if i.category in income_by_category:
            income_by_category[i.category] += i.worth
        else:
            income_by_category[i.category] = i.worth

    expenses_by_category = {}
    for e in expenses:
        if e.category in expenses_by_category:
            expenses_by_category[e.category] += e.worth
        else:
            expenses_by_category[e.category] = e.worth

    return {"income_by_category": income_by_category, "expenses_by_category": expenses_by_category}