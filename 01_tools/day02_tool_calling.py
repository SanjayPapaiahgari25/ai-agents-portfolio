import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from tools import get_current_time

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
    You are an AI assistant.

    You have access to the following tool:

    Tool name: get_current_time
    Description: Returns the current system time as a string.

    When you answer:
    - If the question requires the current time, respond ONLY in JSON:
    {"action": "get_current_time"}
    - Otherwise, respond ONLY in JSON:
    {"action": "answer", "content": "<your answer>"}
"""

USER_PROMPT = "Explain what an AI agent is"


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    temperature = 0.0
)

raw_output = response.choices[0].message.content
print("RAW MODEL OUTPUT:", raw_output)

decision = json.loads(raw_output)

if decision["action"] == "get_current_time":
    tool_result = get_current_time()
    print("TOOL RESULT:", tool_result)

elif decision["action"] == "answer":
    print("MODEL ANSWER:", decision["content"])
