# Python file placeholder
import time
from utils.config_loader import load_config
from utils.logger import log_trade
from utils.notifier import send_discord_notification
from exchanges.binance_api import BinanceAPI
from strategies.moving_average import MovingAverageStrategy

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
            # Obtenir les données de marché
            market_data = binance.get_market_data()

            # Appliquer la stratégie
            signals = strategy.generate_signals(market_data)

            # Effectuer les trades
            for signal in signals:
                if mode == "real":
                    trade_result = binance.execute_trade(signal)
                    log_trade(trade_result, "./logs/trade_logs.json")
                    send_discord_notification(trade_result)
                else:
                    print(f"Test Mode Signal: {signal}")

            time.sleep(60)  # Rafraîchir toutes les minutes
        except Exception as e:
            print(f"Erreur: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
