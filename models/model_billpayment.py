from pydantic import BaseModel


class GPOSBillPayment(BaseModel):
    store: int
    institution: int
    amount: float

class ECOMBillPayment(BaseModel)
    site: int
    customer: str
    institution: int
    amount: float