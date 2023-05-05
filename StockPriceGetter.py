import logging
import os
import requests
import pyodbc
from datetime import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    symbol = req.params.get('symbol')
    if not symbol:
        return func.HttpResponse("Please provide a stock symbol as a parameter.", status_code=400)
    
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]

        # Write the stock price to Azure SQL database
        connection_string = os.environ["SqlConnectionString"]
        with pyodbc.connect(connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO StockPrices (Symbol, Price, Timestamp) VALUES ('{symbol}', {price}, '{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')}')") # Replace StockPrices with your table name
                conn.commit()

        return func.HttpResponse(f"The stock price for {symbol} is {price}.", status_code=200)

    except Exception as e:
        logging.error(e)
        return func.HttpResponse("An error occurred while getting the stock price.", status_code=500)
