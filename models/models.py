from typing import Optional

from pydantic import BaseModel, Field

class ModelPayload(BaseModel):
    product_name: str = Field(alias='productName')
    product_price: float = Field(alias='productPrice')
    product_image: str = Field(alias='productImage')

