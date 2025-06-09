import requests

def notify_n8n(user):
    webhook_url = "http://localhost:5678/webhook/user-created"
    payload = {
        "name": user.first_name,
        "email": user.email
    }
    requests.post(webhook_url, json=payload)
