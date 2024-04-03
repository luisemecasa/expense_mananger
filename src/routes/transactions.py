from fastapi import FastAPI, APIRouter
from pydantic import BaseModel , Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import uuid4
from src.schemas.transaction import Transaction

product_router = APIRouter()


income = []
expenses = []

@product_router.post("/income", tags=["income"])
def add_income(transaction: Transaction):
    income.append(transaction)
    return transaction

@product_router.get("/income", tags=["income"])
def get_income():
    return income

@product_router.delete("/income/{transaction_id}", tags=["income"])
def delete_income(transaction_id: str):
    global income
    income = [i for i in income if i.id != transaction_id]
    return {"message": "Transaction deleted"}

@product_router.post("/expenses", tags=["expenses"])
def add_expense(transaction: Transaction):
    expenses.append(transaction)
    return transaction

@product_router.get("/expenses", tags=["expenses"])
def get_expenses():
    return expenses

@product_router.delete("/expenses/{transaction_id}", tags=["expenses"])
def delete_expense(transaction_id: int):
    global expenses
    expenses = [i for i in expenses if i.id != transaction_id]
    return {"message": "Transaction deleted"}

@product_router.get("/report/basic", tags=["report"])
def basic_report():
    total_income = sum(i.worth for i in income)
    total_expenses = sum(e.worth for e in expenses)
    balance = total_income - total_expenses
    return {"total_income": total_income, "total_expenses": total_expenses, "balance": balance}

@product_router.get("/report/expanded" , tags=["report"])
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

