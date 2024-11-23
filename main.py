import time
import argparse
from utils.config_loader import load_config
from utils.logger import log_trade, log_error
from utils.notifier import send_discord_notification
from exchanges.binance_api import BinanceAPI
from exchanges.bitmart_api import BitmartAPI
from strategies.moving_average import MovingAverageStrategy
from strategies.macd_strategy import MACDStrategy
from utils.risk_management import RiskManagement
from utils.config_loader import load_pairs

# Charger la configuration dynamique
config = load_config("./config/config.json")
trading_pairs = load_pairs()
print(f"Paires de trading : {trading_pairs}")

# Ajout du Leverage
leverage = config["trade_settings"]["leverage"]

# Utiliser les informations d'échange
binance_config = config["exchanges"]["binance"]

# Initialiser la gestion du risque avec la configuration complète
risk_management = RiskManagement(config["trade_settings"])

# Initialiser l'API Binance
binance = BinanceAPI(binance_config)

market_cache = {}
cache_expiry = 60  # Durée de validité du cache en secondes

def get_cached_market_data(exchange):
    global market_cache
    current_time = time.time()

    # Vérifier si le cache est valide
    if "data" in market_cache and current_time - market_cache["timestamp"] < cache_expiry:
        print("Utilisation des données mises en cache.")
        return market_cache["data"]

    # Sinon, récupérer de nouvelles données
    print("Récupération des nouvelles données de marché.")
    data = exchange.get_all_market_data()  # Récupérer toutes les données de marché
    market_cache = {"data": data, "timestamp": current_time}  # Mise à jour du cache
    return data

def get_exchange_from_args():
    parser = argparse.ArgumentParser(description="Choisir l'échange pour le trading")
    parser.add_argument("--exchange", choices=["binance", "bitmart"], default="binance", help="L'échange à utiliser")
    args = parser.parse_args()
    return args.exchange

def main():
    exchange_choice = get_exchange_from_args()
    if exchange_choice == "binance":
        exchange = BinanceAPI(config["exchanges"]["binance"])
        print("Utilisation de Binance")
    elif exchange_choice == "bitmart":
        exchange = BitmartAPI(config["exchanges"]["bitmart"])
        print("Utilisation de Bitmart")
    
    # Mode de fonctionnement
    mode = config["mode"]
    print(f"Bot de trading lancé en mode: {mode}")

    while True:
        try:
            # Récupération optimisée des données de marché
            market_data = get_cached_market_data(exchange)  # Toutes les paires en une seule requête

            for pair in trading_pairs:
                pair_data = market_data.get(pair)  # Utilisation sécurisée avec `.get()`
                if not pair_data:
                    print(f"Données indisponibles ou invalides pour {pair}.")
                    continue

                print(f"Données de marché pour {pair} : {pair_data}")
                # Appliquer les stratégies et poursuivre

                # Appliquer la stratégie
                strategy = MovingAverageStrategy()
                signals = strategy.generate_signals(pair_data)

                # Calcul de la taille de la position
                account_balance = config["trade_settings"]["account_balance"]
                stop_loss_distance = config["trade_settings"]["stop_loss_distance"]
                position_size = risk_management.calculate_position_size() * leverage
                print(f"Taille de la position calculée pour {pair}: {position_size}")

                # Effectuer les trades
                if risk_management.check_max_open_trades(len(signals)):
                    for signal in signals:
                        if mode == "real":
                            trade_result = exchange.place_order(pair, signal, position_size)
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
