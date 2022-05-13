from fastapi import FastAPI
from routers.router_virtualcontent import router as api_router

app = FastAPI()

app.include_router(api_router)