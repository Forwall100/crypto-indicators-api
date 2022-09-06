from fastapi import FastAPI
import uvicorn
from endpoints import sma, ema, rsi, stoch
from utils.constans import HOST, PORT

app = FastAPI()

app.include_router(sma.router)
app.include_router(ema.router)
app.include_router(rsi.router)
app.include_router(stoch.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=PORT,
        host=HOST,
        reload=True
    )
