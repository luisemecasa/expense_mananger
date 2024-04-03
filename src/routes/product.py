from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.product import Product

product_router = APIRouter()


@product_router.get('/',
                   tags=['products'],
                   response_model=List[Product],
                   description="Returns all products stored")
def get_all_products(min_price: float = Query(default=None, min=10, max=5000000),
                     max_price: float = Query(default=None, min=10, max=5000000)) -> List[Product]:
    result = []
    for element in products:
        if min_price is not None and element['price'] < min_price:
            continue
        if max_price is not None and element['price'] > max_price:
            continue
        result.append(element)
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

@product_router.get('/{id}',
                   tags=['products'],
                   response_model=Product,
                   description="Returns data of one specific product")
def get_product(id: int = Path(ge=1, le=5000)) -> Product:
    for element in products:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=status.HTTP_200_OK)
    return JSONResponse(content=None, status_code=status.HTTP_404_NOT_FOUND)

@product_router.post('/',
                    tags=['products'],
                    response_model=dict,
                    description="Creates a new product")
def create_product(product: Product = Body()) -> dict:
    products.append(product.model_dump())
    return JSONResponse(content={
        "message": "The product was created successfully",
        "data": product.model_dump()
    }, status_code=status.HTTP_201_CREATED)

@product_router.put('/{id}',
                   tags=['products'],
                   response_model=dict,
                   description="Updates the data of specific product")
def update_product(id: int = Path(ge=1),
                   product: Product = Body()) -> dict:
    for element in products:
        if element['id'] == id:
            element['name'] = product.name
            element['price'] = product.price
            element['expiration'] = product.expiration
            return JSONResponse(content={
                "message": "The product was updated successfully",
                "data": element
            }, status_code=status.HTTP_200_OK)
    return JSONResponse(content={
        "message": "The product does not exists",
        "data": None
    }, status_code=status.HTTP_404_NOT_FOUND)

@product_router.delete('/{id}',
                      tags=['products'],
                      response_model=dict,
                      description="Removes specific product")
def remove_product(id: int = Path(ge=1)) -> dict:
    for element in products:
        if element['id'] == id:
            products.remove(element)
            return JSONResponse(content={
                "message": "The product was removed successfully",
                "data": None
            }, status_code=status.HTTP_200_OK)
    return JSONResponse(content={
        "message": "The product does not exists",
        "data": None
    }, status_code=status.HTTP_404_NOT_FOUND)

products = [
    {
        "id": 0,
        "name": "Papitas",
        "price": 100,
        "expiration": "2025-01-01"
    },
    {
        "id": 1,
        "name": "Gomitas",
        "price": 200,
        "expiration": None
    },
    {
        "id": 2,
        "name": "Juguitos",
        "price": 300,
        "expiration": "2025-02-02"
    }
]
