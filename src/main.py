from fastapi import FastAPI
import uvicorn

from src.config.lifespan import lifespan
from src.config.middleware import cors_middleware
from src.api import v1

app = FastAPI(
    title="CRM System",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(v1.routers)

cors_middleware(
    app=app
)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=8070
    )