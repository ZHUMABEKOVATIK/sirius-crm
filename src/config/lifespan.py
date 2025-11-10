from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database.database import async_main

@asynccontextmanager
async def lifespan(app: FastAPI):
    await async_main()
    print("Start...")
    yield
    print("End...")