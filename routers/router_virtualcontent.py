from models.model_virtualcontent import VirtualContentRequest
from services.service_virtualcontent import do_virtualcontent_transformation
from fastapi import APIRouter, Request, Body

router = APIRouter(
    prefix="/virtualcontent",
    tags=["virtualcontent"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def buy_virtual_content(
        request: Request,
        parameters: VirtualContentRequest = Body(...)
):
    return await do_virtualcontent_transformation(parameters)
