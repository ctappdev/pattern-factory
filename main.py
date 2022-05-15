from fastapi import FastAPI
from routers.router_virtualcontent import router as virtualcontent
from routers.router_billpayment import router as billpayment

app = FastAPI()

app.include_router(virtualcontent)
app.include_router(billpayment)