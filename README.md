# Introduction
This is the source code for an API that scrapes the Markets Insider page of the T. Row Price Retirement 2060 Trust (Class C)  mutual fund and returns the current price. 
You can find the Markets Insider source page [here](https://markets.businessinsider.com/funds/t-rowe-price-retirement-2060-trust-class-c-us87281n3044).

You can access the API at https://fa-trpwebscraper.azurewebsites.net/

# Running the API locally
1. Clone the repository locally.
2. Create a virtual environment.
3. Run the following commands:

```commandline
cd TRPWebscraper
pip install -r requirements.txt
cd src
uvicorn api:app --host "0.0.0.0" --port 80
```

# Sending a request
Send a request to the URL http://0.0.0.0:80.

# Endpoints
| Endpoint      | HTTP Method | Description                 | Parameters         |
|---------------|-------------|-----------------------------|--------------------|
| `/health`     | GET         | Check the health of the API | None               |
| `/get-pricce` | GET         | Get the price of the MF     | None               |


# Errors
404 - Incorrect URL

500 - There was some issue getting the price

# Samples
## Input
`https://fa-trpwebscraper.azurewebsites.net/get-price`
## Response
```json
{
  "price": "$24.05"
}
```




