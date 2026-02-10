import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI Chat Completions endpoint
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

# HTTP headers (auth + content type)
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

# Request payload 
payload = {
    "model": "gpt-4.1-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain what an AI agent is in simple terms."}
    ],
    "temperature": 0.2
}

# Make the API request
response = requests.post(
    url=OPENAI_URL,
    headers=headers,
    json=payload,
    timeout=30
)

# Convert response to JSON
response_json = response.json()

print(response_json)
print(response_json["choices"][0]["message"]["content"])