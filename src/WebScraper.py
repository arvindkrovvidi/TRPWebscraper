from http.client import HTTPException
from fastapi import HTTPException, status
from bs4 import BeautifulSoup
import requests


class WebScraper:
    def __init__(self, page_url):
        self.url = page_url

    def get_soup(self):
        try:
            page_to_scrape = requests.get(self.url)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Error trying to connect to {self.url}')
        else:
            return BeautifulSoup(page_to_scrape.text, 'html.parser')