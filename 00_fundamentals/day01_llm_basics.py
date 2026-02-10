import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain what an AI agent is in simple terms."}
    ],
    temperature = 0.2
)

print(response.choices[0].message.content)