#!/bin/bash
echo "Installation des dépendances..."
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt

echo "Configuration terminée. Utilisez './setup/start_bot.sh' pour lancer le bot."
