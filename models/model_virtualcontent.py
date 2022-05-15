from pydantic import BaseModel, Field
from models.model_gpos import GPOSREquest
from models.model_ecom import ECOMREquest
from typing import Union


class VirtualContentRequest(BaseModel):
    detail: Union[GPOSREquest, ECOMREquest] = Field(..., discriminator='channel')


class VirtualContentModel(BaseModel):
    trn_type: str
    entity: int
    retailer: str
    channel: str
    provider: int
    product: str
    amount: float

    @classmethod
    def do_gpos_transformation(cls, payload: VirtualContentRequest):
        return "GPOS Virtual Content Payload"
        # return payload

    @classmethod
    def do_ecom_transformation(cls, payload: VirtualContentRequest):
        return "ECOM Virtual Content Payload"
        # return payload
