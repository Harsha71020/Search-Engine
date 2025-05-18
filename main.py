from fastapi import FastAPI, Query
from backend.search_router import router as search_router

app = FastAPI()
app.include_router(search_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Distributed Search API"}