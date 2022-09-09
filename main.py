from fastapi import FastAPI
import uvicorn
from endpoints import sma, ema, rsi, stoch, stoch_rsi
from utils.constans import HOST, PORT

app = FastAPI()

app.include_router(sma.router)
app.include_router(ema.router)
app.include_router(rsi.router)
app.include_router(stoch.router)
app.include_router(stoch_rsi.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=PORT,
        host=HOST,
        reload=True
    )
