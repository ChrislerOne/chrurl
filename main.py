from fastapi import FastAPI
from v1.routes import shortener

app = FastAPI()

app.include_router(
    shortener.router, 
    tags=["URL Shortening"]
)

