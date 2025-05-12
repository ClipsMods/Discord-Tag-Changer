import time
import requests
import signal
import sys

# List of Guild IDs
GUILD_IDS = [
"PASTE GUILD ID HERE",
"PASTE GUILD ID HERE",
"PASTE GUILD ID HERE",
"Don't Skid lmao",
"Example-714174111752126605",
"1369736569463771226",
"Hey Dumbass, no comment at the end here"
]

# User authorization token


AUTH_TOKEN = ""

# Handle CTRL+C gracefully
def signal_handler(sig, frame):
    print("Script terminated by user")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Starting tag rotation... -- https://github.com/ClipsMods")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '/',
    'Content-Type': 'application/json',
    'Authorization': AUTH_TOKEN,
    'Origin': 'https://discord.com/',
    'Referer': 'https://discord.com/channels/@me'
}

url = "https://discord.com/api/v9/users/@me/clan"

# Loop forever
while True:
    for guild_id in GUILD_IDS:
        payload = {
            "identity_guild_id": guild_id,
            "identity_enabled": True
        }

        response = requests.put(url, json=payload, headers=headers)

        if 200 <= response.status_code < 300:
            # Request succeeded
            pass
        else:
            print(f"Request failed for guild {guild_id} with status code {response.status_code}:")
            print(response.text)

        time.sleep(1)  # Wait before next request
