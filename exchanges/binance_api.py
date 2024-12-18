# binance_api.py
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

    def execute_trade(self, signal, symbol, quantity, order_type="MARKET"):
        """
        Exécute un trade basé sur le signal.
        :param signal: 'buy' ou 'sell'
        :param symbol: Paire de trading (ex: 'BTCUSDT')
        :param quantity: Quantité à trader
        :param order_type: Type d'ordre (par défaut "MARKET")
        :return: Résultat de l'exécution de l'ordre
        """
        side = "BUY" if signal == "buy" else "SELL"
        return self.place_order(symbol, side, quantity, order_type)
