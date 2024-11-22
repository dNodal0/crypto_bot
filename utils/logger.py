# Python file placeholder
import json
from datetime import datetime

def log_trade(trade, filepath):
    trade["timestamp"] = datetime.utcnow().isoformat()
    with open(filepath, 'a') as file:
        file.write(json.dumps(trade) + "\n")
