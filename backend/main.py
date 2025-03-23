from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routers import home, stock, chat
from backend.utils.logger import setup_logger
import os

app = FastAPI()
logger = setup_logger()

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(home.router)
app.include_router(stock.router)
app.include_router(chat.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
