from typing import Union, Literal
from pydantic import BaseModel, Field


class VirtualContentDetails(BaseModel):
    trn_type: Literal["VirtualContent"]
    provider_no: int
    product_code: int
    amount: float


class BillPaymentDetails(BaseModel):
    trn_type: Literal["BillPayment"]
    provider_no: int
    account_no: int
    amount: float


class ECOMREquest(BaseModel):
    site_id: int
    retailer: str
    channel: Literal["ECOM"]
    payment_details: Union[VirtualContentDetails, BillPaymentDetails] = Field(..., discriminator='trn_type')
