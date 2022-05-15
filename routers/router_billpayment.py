from models.model_billpayment import BillPaymentRequest
from services.service_billpayment import do_billpayment_transformation
from fastapi import APIRouter, Request, Body
from pydantic import Json

router = APIRouter(
    prefix="/billpayment",
    tags=["billpayment"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def do_pay_billpayment(
        request: Request,
        parameters: BillPaymentRequest = Body(...)
):
    return await do_billpayment_transformation(parameters)
