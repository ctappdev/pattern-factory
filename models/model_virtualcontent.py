from typing import Literal, Union
from pydantic import BaseModel, Field
from dataclasses import dataclass


@dataclass
class GPOSVirtualContent(BaseModel):
    tag: Literal["gpos"]
    product: str
    amount: float


@dataclass
class ECOMVirtualContent(BaseModel):
    tag: Literal["ecom"]
    product_type: int
    value: float


@dataclass
class VirtualContent(BaseModel):
    store: int
    retailer: str
    detail: Union[GPOSVirtualContent, ECOMVirtualContent] = Field(..., discriminator='tag')


@dataclass
class VirtualContentModel:
    store: int
    retailer: str
    product: str
    amount: float

    def __init__(self, store, retailer, product, amount):
        self.store = store
        self.retailer = retailer
        self.product = product
        self.amount = amount

    @classmethod
    def do_gpos_transformation(cls, payload: VirtualContent):
        return cls(payload.store, payload.retailer, payload.detail.product, payload.detail.amount)

    @classmethod
    def do_ecom_transformation(cls, payload: VirtualContent):
        return cls(payload.store, payload.retailer, payload.detail.product_type, payload.detail.amount)
