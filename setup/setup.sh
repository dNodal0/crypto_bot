#!/bin/bash
echo "Installation des dépendances..."
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt

echo "Génération du fichier config.json..."
python3 generate_config.py

echo "Configuration terminée."