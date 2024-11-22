import os
import json
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv(dotenv_path="./secrets/.env")

def load_pairs(filepath="./config/pairs.json"):
    """
    Charge la liste des paires crypto depuis un fichier JSON.
    """
    with open(filepath, "r") as file:
        return json.load(file)

def load_config(config_path="./config/config.json"):
    """
    Charge la configuration JSON et remplace les variables d'environnement dynamiques.
    """
    with open(config_path, "r") as file:
        config = json.load(file)

    # Remplacement des placeholders (${VARIABLE}) par les variables d'environnement
    for exchange_name, exchange_config in config.get("exchanges", {}).items():
        if exchange_name in ["binance", "bitmart", "bybit"]:
            exchange_config["api_key"] = os.getenv(f"{exchange_name.upper()}_API_KEY")
            exchange_config["api_secret"] = os.getenv(f"{exchange_name.upper()}_API_SECRET")

    # Remplacement des placeholders globaux (par ex. Discord)
    discord_config = config.get("discord", {})
    if "webhook_url" in discord_config:
        discord_config["webhook_url"] = os.getenv("DISCORD_WEBHOOK_URL", discord_config["webhook_url"])

    return config