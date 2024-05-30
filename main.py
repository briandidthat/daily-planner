import os

from pprint import pprint

from fastapi import FastAPI
from routers import tasks

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

app = FastAPI()
app.include_router(tasks.router)