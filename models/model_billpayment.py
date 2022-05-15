from pydantic import BaseModel, Field
from models.model_gpos import GPOSREquest
from models.model_ecom import ECOMREquest
from typing import Union


class BillPaymentRequest(BaseModel):
    detail: Union[GPOSREquest, ECOMREquest] = Field(..., discriminator='channel')


class BillPaymentModel(BaseModel):
    trn_type: str
    entity: int
    retailer: str
    channel: str
    provider: int
    account: str
    amount: float

    @classmethod
    def do_gpos_transformation(cls, payload: BillPaymentRequest):
        return "GPOS Bill Payment Payload"
        # return payload

    @classmethod
    def do_ecom_transformation(cls, payload: BillPaymentRequest):
        return "ECOM Bill Payment Payload"
        # return payload
