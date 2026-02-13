import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import get_current_time

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
    You are an autonomousAI agent.

    You have access to the following tool:

    Tool: get_current_time
    Description: Returns the current system time

    You must follow this format:

    Thought: Explain your reasoning.
    Action: The tool name (or "None")
    Action Input: Input for the tool (or "None")

    OR

    Final Answer: Your final response to the user.

    Do not skip steps. 
"""

user_question = "What time is it right now?"

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_question}
]

while True:
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages,
        temperature = 0.0
    )

    output = response.choices[0].message.content
    print("\nMODEL OUTPUT:\n", output)

    if "Final Answer:" in output:
        break
    
    # Parse Action

    if "Action: get_current_time" in output:
        tool_result = get_current_time()
        print("TOOL RESULT:", tool_result)

        messages.append(
            {
                "role": "assistant",
                "content": output
            }
        )

        messages.append(
            {
                "role": "user",
                "content": f"observation: {tool_result}"
            }
        )

    else:
        print("No valid action found. Stopping.")
        break