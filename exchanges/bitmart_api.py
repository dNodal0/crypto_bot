import requests

class BitmartAPI:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.base_url = "https://api-cloud.bitmart.com"
        # Ajout du levier avec valeur par défaut
        self.leverage = config.get("trade_settings", {}).get("leverage", 1)

    def get_market_data(self, symbol):
        url = f"{self.base_url}/spot/v1/ticker"
        response = requests.get(url, params={"symbol": symbol})
        return response.json()

    def set_leverage(self, symbol):
        url = f"{self.base_url}/futures/v1/set_leverage"
        headers = {"X-BM-APIKEY": self.api_key}
        payload = {
            "symbol": symbol,
            "leverage": self.leverage
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def place_order(self, symbol, side, quantity):
        # Set leverage first
        self.set_leverage(symbol)
        
        url = f"{self.base_url}/futures/v1/submit_order"
        headers = {"X-BM-APIKEY": self.api_key}
        payload = {
            "symbol": symbol,
            "side": side,
            "size": quantity,
            "type": "market"
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
