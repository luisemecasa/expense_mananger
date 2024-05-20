from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandler
from src.routes.transactions import product_router
from src.routes.user import user_router
from src.config.database import init_db

app = FastAPI()

app.title = "Expense Manager API"
app.summary = "Expense Manager API REST API with FastAPI and Python"
app.description = "This is a demonstration of API REST using Python"
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
    {
        "name": "users",
        "description": "Operations with user management",
    }
]

app.add_middleware(ErrorHandler)
app.include_router(product_router, prefix="/products")
app.include_router(user_router, prefix="/users")

@app.on_event("startup")
def on_startup():
    init_db()  # Inicializa la base de datos aquí
