from pathlib import Path
import sys

root = Path.cwd()
sys.path.append(str(root))

from fastapi import FastAPI
from src import router
import uvicorn

app = FastAPI(title="Web scraper API", description="A web scraper API to get the price of TRP2060")

app.include_router(router.router)

if __name__=="__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)

