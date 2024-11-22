import os
import json
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv(dotenv_path="./secrets/.env")

def generate_config():
    # Récupérer les clés API
    config_data = {
        "mode": "test",  # ou "real"
        "exchanges": {
            "binance": {
                "api_key": os.getenv("BINANCE_API_KEY"),
                "api_secret": os.getenv("BINANCE_API_SECRET"),
                "use_testnet": True
            },
            "bitmart": {
                "api_key": os.getenv("BITMART_API_KEY"),
                "api_secret": os.getenv("BITMART_API_SECRET")
            },
            "bybit": {
                "api_key": os.getenv("BYBIT_API_KEY"),
                "api_secret": os.getenv("BYBIT_API_SECRET")
            }
        },
        "trade_settings": {
            "risk_per_trade": 0.01,
            "max_open_trades": 5
        },
        "discord": {
            "webhook_url": os.getenv("DISCORD_WEBHOOK_URL", "https://your_default_webhook_url")
        }
    }

    # Écrire les données dans config.json
    with open("./config/config.json", "w") as config_file:
        json.dump(config_data, config_file, indent=4)

    print("config.json généré avec succès !")

if __name__ == "__main__":
    generate_config()
