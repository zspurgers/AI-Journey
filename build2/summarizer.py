import os
import anthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

file = open("sample.txt", "r")
file_contents = file.read()
file.close()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
  model = "claude-opus-4-8",
  max_tokens = 1000,
  messages = [{"role": "user","content": f"Please summarize the following text:\n\n{file_contents}"}])

print(message.content[0].text)
