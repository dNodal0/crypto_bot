# Python file placeholder
import requests

def send_discord_notification(message):
    webhook_url = "https://discord.com/api/webhooks/votre_webhook_id/votre_token"
    payload = {"content": f"🚀 Trade Notification: {message}"}
    requests.post(webhook_url, json=payload)
