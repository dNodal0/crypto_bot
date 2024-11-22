#!/bin/bash
echo "Lancement du bot..."
nohup python3 main.py > logs/bot_output.log 2>&1 &
echo "Bot lancé avec succès."
