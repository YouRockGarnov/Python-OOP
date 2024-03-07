from fastapi import FastAPI
from bs4 import BeautifulSoup
import aiohttp


app = FastAPI()


@app.get("/scrape")
async def scrape(url: str):
    # TODO: Напишите код здесь
    raise NotImplementedError
