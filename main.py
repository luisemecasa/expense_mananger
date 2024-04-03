from src.middlewares.error_handler import ErrorHandler;
from src.routes.transactions import product_router
from fastapi import FastAPI

app = FastAPI()

app.title = "Expense Manager API"
app.summary = "Expense Manager API REST API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.2"
app.contact = {
 "name": "Johan Polo and Luis Canon",
} 

app.tags_metadata = [
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

app.add_middleware(ErrorHandler)
app.include_router(prefix="/products", router=product_router)