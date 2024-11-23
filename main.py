import time
from utils.config_loader import load_config
from utils.logger import log_trade, log_error
from utils.notifier import send_discord_notification
from exchanges.binance_api import BinanceAPI
from strategies.moving_average import MovingAverageStrategy
from strategies.macd_strategy import MACDStrategy
from utils.risk_management import RiskManagement
from utils.config_loader import load_pairs

# Charger la configuration dynamique
config = load_config("./config/config.json")
trading_pairs = load_pairs()
print(f"Paires de trading : {trading_pairs}")

# Utiliser les informations d'échange
binance_config = config["exchanges"]["binance"]
# print("Binance API Key:", binance_config["api_key"])
# print("Binance API Secret:", binance_config["api_secret"])

# Initialiser la gestion du risque avec la configuration complète
risk_management = RiskManagement(config["trade_settings"])


# Initialiser l'API Binance
binance = BinanceAPI(binance_config)

def main():
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
                strategy = MovingAverageStrategy()  # Exemple, tu peux en choisir une autre
                signals = strategy.generate_signals(market_data)

                # Vérifier si la taille des positions est compatible avec le risque
                account_balance = config["trade_settings"]["account_balance"]
                stop_loss_distance = config["trade_settings"]["stop_loss_distance"]
                position_size = risk_management.calculate_position_size()
                print(f"Taille de la position calculée pour {pair}: {position_size}")

                # Effectuer les trades si le nombre de trades ouverts est inférieur à la limite
                if risk_management.check_max_open_trades(len(signals)):
                    for signal in signals:
                        if mode == "real":
                            trade_result = binance.place_order(pair, signal, position_size)
                            log_trade(trade_result, "./logs/trade_logs.json")
                            send_discord_notification(trade_result)
                        else:
                            print(f"Test Mode Signal pour {pair} : {signal}")
                            log_trade({"signal": signal}, "./logs/trade_logs.json")  # Log de test
                else:
                    print("Limite de trades ouverts atteinte")

            time.sleep(60)  # Rafraîchir toutes les minutes
        except Exception as e:
            print(f"Erreur dans la fonction principale : {e}")
            log_error(e, "./logs/error_logs.json")

if __name__ == "__main__":
    main()
