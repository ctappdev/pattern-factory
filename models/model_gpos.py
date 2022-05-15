from typing import Union, Literal
from pydantic import BaseModel, Field


class VirtualContentDetails(BaseModel):
    trn_type: Literal["VirtualContent"]
    provider: int
    product: int
    amount: float


class BillPaymentDetails(BaseModel):
    trn_type: Literal["BillPayment"]
    provider: int
    account: int
    amount: float


class GPOSREquest(BaseModel):
    store: int
    till: int
    retailer: str
    channel: Literal["GPOS"]
    payment_details: Union[VirtualContentDetails, BillPaymentDetails] = Field(..., discriminator='trn_type')
