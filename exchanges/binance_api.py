# Python file placeholder
from binance.client import Client

class BinanceAPI:
    def __init__(self, config):
        self.client = Client(config["api_key"], config["api_secret"])
        self.use_testnet = config.get("use_testnet", False)
        if self.use_testnet:
            self.client.API_URL = "https://testnet.binance.vision/api"

    def get_market_data(self, symbol):
        return self.client.get_symbol_ticker(symbol=symbol)

    def place_order(self, symbol, side, quantity, order_type="MARKET"):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )
