# Python file placeholder
import requests

class BybitAPI:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.base_url = "https://api.bybit.com"

    def get_market_data(self, symbol):
        url = f"{self.base_url}/v2/public/tickers"
        response = requests.get(url, params={"symbol": symbol})
        return response.json()

    def place_order(self, symbol, side, quantity):
        url = f"{self.base_url}/v2/private/order/create"
        payload = {
            "api_key": self.api_key,
            "symbol": symbol,
            "side": side,
            "order_type": "Market",
            "qty": quantity
        }
        response = requests.post(url, json=payload)
        return response.json()
