import os
import openai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test
print("OpenAI API Key loaded:", openai.api_key is not None)

# Optional: try a quick GPT call
try:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hello in one sentence"}],
        temperature=0
    )
    print("GPT response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
