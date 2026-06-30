import sys #imports the sys library so the scipt can access command line arguments
import os
from pathlib import Path #imports the Path library to work with file paths

import anthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

output_file = open("index.md","w", encoding="utf-8")

if len(sys.argv) < 2:
  print("You are missing the folder path. Please enter it here")
  folder_path = Path(input())
else:
  folder_path = Path(sys.argv[1])

if not folder_path.exists():
    print("This folder path does not exist")
    sys.exit()
elif not folder_path.is_dir():
    print("The filepath is not a directory")
    sys.exit()
else:  
    #folder_path = r"C:\Users\zacha\War Room\Code\Projects\AI-Journey\build3\sample_projects" #pulls in the "r"aw data of the hardcoded folder
  info_pull = Path(folder_path) #pull the object so that info_pull points to the folder

  summaries = []

  for item in info_pull.glob("*.md"): #looks through each file in info_pull and prints if .md file 
    file = open(item, "r", encoding="utf-8")
    file_contents = file.read()
  
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
  
    message = client.messages.create(
      model = "claude-opus-4-8",
      max_tokens = 1000,
      messages = [{"role" : "user", "content" : f"Please summarize the following text:\n\n{file_contents} "}]
    )
  
    output_file.write(f"## {item.name}\n\n")
    output_file.write(message.content[0].text + "\n\n")

    summaries.append((item.name,message.content[0].text))

    file.close()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
  
message = client.messages.create(
  model = "claude-opus-4-8",
  max_tokens = 1000,
  messages = [{"role" : "user", "content" : f"Please summarize the following text:\n\n{summaries} "}]
)  

output_file.write(message.content[0].text)
output_file.write("\n")

output_file.close()