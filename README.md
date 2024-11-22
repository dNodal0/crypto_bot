# Trading Bot

Automated trading bot for cryptocurrencies.

# Trading Bot

## Description
Ce projet est un bot de trading automatisé conçu pour trader les cryptomonnaies sur plusieurs plateformes d'échange (Binance, Bitmart, Bybit). Le bot est modulaire, facile à configurer, et peut être utilisé en mode test ou réel.

## Structure du Projet
```plaintext
trading_bot
├── LICENSE
├── README.md
├── exchanges
│   ├── binance_api.py
│   ├── bitmart_api.py
│   ├── bybit_api.py
├── main.py
├── requirements.txt
├── strategies
│   ├── moving_average.py
│   ├── rsi_strategy.py
│   ├── config_example.json
├── utils
│   ├── config_loader.py
│   ├── logger.py
│   ├── notifier.py
├── logs
│   ├── trade_logs.json
├── config
│   ├── config.json
├── setup
│   ├── setup.sh
│   ├── start_bot.sh
├── .gitignore
├── CONTRIBUTING.md
└── secrets
    └── .env
```

## Prérequis
1. Python 3.8 ou supérieur
2. Pip (Gestionnaire de packages Python)
3. Un compte sur les exchanges pris en charge (Binance, Bitmart, Bybit)
4. Une clé API pour chaque exchange

## Installation
### Étape 1: Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/trading_bot.git
cd trading_bot
```

### Étape 2: Installer les dépendances
```bash
pip install -r requirements.txt
```

### Étape 3: Configurer le fichier `.env`
Ajoutez vos clés API dans `secrets/.env` :
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

### Étape 4: Configurer `config.json`
Modifiez `config/config.json` pour définir les paramètres du bot, comme le mode, le risque par trade, et l'URL Discord pour les notifications.

## Utilisation
### Mode Test
Pour exécuter le bot en mode test :
```bash
python main.py
```

### Mode Réel
Pour exécuter le bot en mode réel, mettez `"mode": "real"` dans `config/config.json`, puis lancez :
```bash
python main.py
```

## Automatisation
Utilisez le script `setup/start_bot.sh` pour démarrer le bot en arrière-plan :
```bash
bash setup/start_bot.sh
```

Vous pouvez également ajouter une tâche Cron pour lancer le bot automatiquement :
```bash
@reboot /chemin/vers/setup/start_bot.sh
```

## Logs
Les logs des transactions sont enregistrés dans `logs/trade_logs.json`. Les notifications sont également envoyées à votre webhook Discord.

## Contribuer
Voir le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus d'informations.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
