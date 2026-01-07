from fastapi import FastAPI, HTTPException
from .models import Product


app = FastAPI(title="Product Service")

FAKE_PRODUCTS_DB = {
    1: Product(id= 1, name="MacBook", price=3500.0),
    2: Product(id= 2, name="iPhone", price=2500.0)
}


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = FAKE_PRODUCTS_DB.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product