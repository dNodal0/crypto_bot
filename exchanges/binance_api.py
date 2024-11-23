from binance.client import Client

class BinanceAPI:
    def __init__(self, config):
        self.client = Client(config["api_key"], config["api_secret"])
        self.use_testnet = config.get("use_testnet", False)
        if self.use_testnet:
            self.client.API_URL = "https://testnet.binance.vision/api"
    
    def get_all_market_data(self):
        """
        Récupère les données de marché pour toutes les paires disponibles.
        :return: Dictionnaire des données de marché par symbole
        """
        try:
            response = self.client.get_all_tickers()  # API Binance
            if not response:
                print("Erreur : aucune donnée de marché récupérée.")
                return {}
            return {item['symbol']: {"price": float(item['price'])} for item in response}
        except Exception as e:
            print(f"Erreur lors de la récupération des données de marché : {e}")
            return {}

    def place_order(self, symbol, side, quantity, order_type="MARKET", leverage=2, isolated=True):
        # Set leverage for isolated margin
        self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
        if isolated:
            self.client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity, positionSide='BOTH')
        else:
            self.client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)

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
