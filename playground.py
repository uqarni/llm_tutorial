from openai import OpenAI

###this is all so that we can securely reference our api key
import os 
from dotenv import load_dotenv
load_dotenv()


openai_client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
name = "John"
system_prompt = f"Your name is {name}. You are a joker who tells jokes about camels. Make sure your response is only one short sentence."
formatted_system_prompt = {"role": "system", "content": system_prompt}
messages = []
messages.append(formatted_system_prompt)


response = openai_client.chat.completions.create(
    model="gpt-4o",
    temperature = 0,
    max_tokens = 100,
    messages=messages,
)

print(response.choices[0].message.content)