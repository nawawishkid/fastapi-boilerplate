from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.user.router import router as user_router

app = FastAPI(title="FastAPI Boilerplate")
v1_router = APIRouter()

v1_router.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(v1_router, prefix="/v1")
