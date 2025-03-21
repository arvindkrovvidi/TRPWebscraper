from fastapi import FastAPI
import router

app = FastAPI(title="Web scraper API", description="A web scraper API to get the price of TRP2060")

app.include_router(router.router)

