from typing import Optional

from pydantic import BaseModel, Field

class ModelPayload(BaseModel):
    product_name: str = Field(alias='productName')
    product_price: float = Field(alias='productPrice')
    product_image: str = Field(alias='productImage')


class ScrapeRequest(BaseModel):
    url: str = Field(alias="url")
    page_no: int = Field(alias="page_no")