        # fastapi run main:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI
from pydantic import EmailStr
from database import get_db, create_tables

app = FastAPI()

# Create database tables on startup
create_tables()

@app.get("/")
async def root():
    return {"Hello": "World"}