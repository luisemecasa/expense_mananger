from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.schemas.transaction import Transaction as TransactionSchema
from src import models, schemas
from src.config.database import SessionLocal

product_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@product_router.post("/income", tags=["income"])
def add_income(transaction: TransactionSchema, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@product_router.get("/income", tags=["income"])
def get_income(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).filter(models.Transaction.category == 'Salary').all()
    return transactions

@product_router.delete("/income/{transaction_id}", tags=["income"])
def delete_income(transaction_id: int, db: Session = Depends(get_db)):
    db.query(models.Transaction).filter(models.Transaction.id == transaction_id).delete()
    db.commit()
    return {"message": "Transaction deleted"}

@product_router.post("/expenses", tags=["expenses"])
def add_expense(transaction: TransactionSchema, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@product_router.get("/expenses", tags=["expenses"])
def get_expenses(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).filter(models.Transaction.category == 'expense').all()
    return transactions

@product_router.delete("/expenses/{transaction_id}", tags=["expenses"])
def delete_expense(transaction_id: int, db: Session = Depends(get_db)):
    db.query(models.Transaction).filter(models.Transaction.id == transaction_id).delete()
    db.commit()
    return {"message": "Transaction deleted"}

@product_router.get("/report/basic", tags=["report"])
def basic_report(db: Session = Depends(get_db)):
    total_income = db.query(func.sum(models.Transaction.worth)).filter(models.Transaction.category == 'Salary').scalar()
    total_expenses = db.query(func.sum(models.Transaction.worth)).filter(models.Transaction.category == 'expense').scalar()
    balance = (total_income or 0) - (total_expenses or 0)
    return {"total_income": total_income, "total_expenses": total_expenses, "balance": balance}

@product_router.get("/report/expanded", tags=["report"])
def expanded_report(db: Session = Depends(get_db)):
    income_by_category = db.query(models.Transaction.category, func.sum(models.Transaction.worth)).filter(models.Transaction.category == 'Salary').group_by(models.Transaction.category).all()
    expenses_by_category = db.query(models.Transaction.category, func.sum(models.Transaction.worth)).filter(models.Transaction.category == 'expense').group_by(models.Transaction.category).all()
    return {"income_by_category": dict(income_by_category), "expenses_by_category": dict(expenses_by_category)}
