from fastapi import APIRouter

routers = APIRouter(prefix="/v1")

@routers.get("/home")
async def home_v1():
    return {'data': "v1 home"}