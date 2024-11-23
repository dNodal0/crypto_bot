# Python file placeholder
import json
import time
from datetime import datetime

def log_trade(trade, filepath):
    trade["timestamp"] = datetime.utcnow().isoformat()
    with open(filepath, 'a') as file:
        file.write(json.dumps(trade) + "\n")

def log_error(error, filepath):
    """
    Enregistre les erreurs dans un fichier JSON.
    
    :param error: Exception ou message d'erreur
    :param filepath: Chemin du fichier de logs
    """
    try:
        with open(filepath, "a") as log_file:
            log_file.write(json.dumps({
                "error": str(error),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }) + "\n")
    except IOError as io_err:
        print(f"Erreur lors de la journalisation dans {filepath}: {io_err}")