from src.middlewares.error_handler import ErrorHandler;
from src.routes.product import product_router

app.add_middleware(ErrorHandler)
app.include_router(prefix="/products", router=product_router)