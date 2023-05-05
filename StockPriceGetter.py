import requests

def main(req):
    symbol = req.params.get('symbol')
    if not symbol:
        return 'Please provide a stock symbol in the query string.'

    url = f'https://finance.yahoo.com/quote/{symbol}/'
    response = requests.get(url)

    if response.status_code != 200:
        return f'Error retrieving stock data for {symbol}'

    start_index = response.text.find('data-reactid="50">') + len('data-reactid="50">')
    end_index = response.text.find('</span>', start_index)
    price = response.text[start_index:end_index]

    return f'The current price of {symbol} is {price}'
