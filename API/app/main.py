from fastapi import FastAPI
from router import api_f

app = FastAPI()
app.include_router(api_f)