from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router

app = FastAPI(title="Yoko_tz", openapi_url="/openapi.json")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=["*"],
)


app.include_router(api_router, prefix="")
