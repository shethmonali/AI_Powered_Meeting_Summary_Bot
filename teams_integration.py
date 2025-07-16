import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_summary_to_teams(summary):
    webhook_url = os.getenv("TEAMS_WEBHOOK_URL")
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "text": f"📋 *Meeting Summary:*\n\n{summary}"
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("✅ Summary successfully posted to Teams!")
    else:
        print(f"❌ Failed to send summary to Teams: {response.status_code} - {response.text}")
