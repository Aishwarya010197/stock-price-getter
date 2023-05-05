# stock-price-getter
Get's the stock prices from yahoo finance api

The main function is the entry point for the Azure Function. It takes a single parameter, req, which is the HTTP request that triggered the function.

We extract the symbol query parameter from the request. If it's not provided, we return an error message.

We construct the URL to retrieve the stock data for the given symbol using Yahoo Finance's API.

We make a GET request to the URL and check the response status code. If it's not 200 (OK), we return an error message.

We use string manipulation to extract the stock price from the HTML response. The start_index variable finds the starting index of the price in the HTML, and the end_index variable finds the ending index. We then use slicing to extract the price string.

Finally, we return a message with the current price of the stock symbol.
