# Python file placeholder
import requests

class BitmartAPI:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.base_url = "https://api-cloud.bitmart.com"

    def get_market_data(self, symbol):
        url = f"{self.base_url}/spot/v1/ticker"
        response = requests.get(url, params={"symbol": symbol})
        return response.json()

    def place_order(self, symbol, side, quantity):
        url = f"{self.base_url}/spot/v1/submit_order"
        headers = {"X-BM-KEY": self.api_key}
        payload = {
            "symbol": symbol,
            "side": side,
            "size": quantity,
            "type": "market"
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
