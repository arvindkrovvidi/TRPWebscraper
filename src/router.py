from fastapi import HTTPException, status

from fastapi import APIRouter
from src.WebScraper import WebScraper
from src.logger import logger


router = APIRouter()


@router.get("/health")
async def root():
    return {"status": "UP"}


@router.get("/get-price")
async def get_trp_price():
    logger.info(f'Entered API')
    trpe_market_insider_url = 'https://markets.businessinsider.com/funds/t-rowe-price-retirement-2060-trust-class-c-us87281n3044'
    scraper = WebScraper(trpe_market_insider_url)
    try:
        soup = scraper.get_soup()
    except HTTPException as e:
        logger.error(str(e), exc_info=True)
        return {'error': str(e), "status_code": e.status_code}
    except Exception as e:
        logger.error(f'An unexpected error has occurred!', exc_info=True)
        return {'error': 'An unexpected error has occurred!', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR}
    else:
        current_price = soup.findAll('span', attrs={'class':'price-section__current-value'})[0].text
        output = {"price": "$" + current_price}
        return output


