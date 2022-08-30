from fastapi import FastAPI
import uvicorn
from endpoints import sma, ema, rsi

app = FastAPI()

app.include_router(sma.router)
app.include_router(ema.router)
app.include_router(rsi.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        host="127.0.0.1",
        reload=True
    )