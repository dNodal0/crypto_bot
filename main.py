# Python file placeholder
import time
from utils.config_loader import load_config
from utils.logger import log_trade, log_error
from utils.notifier import send_discord_notification
from exchanges.binance_api import BinanceAPI
from strategies.moving_average import MovingAverageStrategy
from strategies.macd_strategy import MACDStrategy
from utils.config_loader import load_config, load_pairs
from utils.risk_management import RiskManagement

# Charger la configuration dynamique
config = load_config()
trading_pairs = load_pairs()
print(f"Paires de trading : {trading_pairs}")

# Utiliser les informations d'échange
binance_config = config["exchanges"]["binance"]
print("Binance API Key:", binance_config["api_key"])
print("Binance API Secret:", binance_config["api_secret"])

# Exemple d'intégration
from exchanges.binance_api import BinanceAPI
binance = BinanceAPI(binance_config)

def main():
    # Charger la configuration
    config = load_config("./config/config.json")

    # Initialiser les exchanges
    binance = BinanceAPI(config["exchanges"]["binance"])

    # Choisir une stratégie
    strategy = MovingAverageStrategy()

    # Mode de fonctionnement
    mode = config["mode"]
    print(f"Bot de trading lancé en mode: {mode}")

    while True:
        try:
            for pair in trading_pairs:
                # Obtenir les données de marché pour chaque paire
                market_data = binance.get_market_data(pair)
                print(f"Données de marché pour {pair} : {market_data}")

                # Appliquer la stratégie
                signals = strategy.generate_signals(market_data)

                # Effectuer les trades
                for signal in signals:
                    if mode == "real":
                        trade_result = binance.execute_trade(signal)
                        log_trade(trade_result, "./logs/trade_logs.json")
                        send_discord_notification(trade_result)
                    else:
                        print(f"Test Mode Signal pour {pair} : {signal}")

            time.sleep(60)  # Rafraîchir toutes les minutes
        except Exception as e:
            print(f"Erreur dans la fonction principale : {e}")
            log_error(e, "./logs/error_logs.json")

if __name__ == "__main__":
    main()
