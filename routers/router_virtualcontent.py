from models.model_virtualcontent import VirtualContent
from services.service_virtual_content import do_virtual_content_transformation
from fastapi import APIRouter, Request, Body
from pydantic import Json

router = APIRouter(
    prefix="/virtualcontent",
    tags=["virtualcontent"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def buy_virtual_content(
        request: Request,
        parameters: VirtualContent = Body(...)
):
    return await do_virtual_content_transformation(parameters)
