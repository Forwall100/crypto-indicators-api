import re
from fastapi import FastAPI
import uvicorn
from endpoints import sma

app = FastAPI()

app.include_router(sma.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        host="127.0.0.1",
        reload=True
    )