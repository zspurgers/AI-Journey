"""
Build 4 — AI Onboarding Assistant (Day 2 slice)

Loads every doc in docs/, sends them to Claude along with a question,
and answers strictly from those docs -- saying "I don't know" when the
answer isn't in there.
"""

import os
import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# The knowledge base: every .md file lives in the docs/ folder next to this script.
DOCS_DIR = Path(__file__).parent / "docs"

SYSTEM_PROMPT = (
    "You are an onboarding assistant for Meridian Software. Answer the "
    "employee's question using ONLY the company documents provided below. "
    "If the documents don't contain the answer, say \"I don't know -- that's "
    "not covered in our onboarding docs\" instead of guessing.\n\n"
)


def load_doc(filename):
    """Read one markdown doc from the docs folder and return its text."""
    path = DOCS_DIR / filename
    return path.read_text(encoding="utf-8")


def load_all_docs():
    """Read every .md file in the docs folder and combine them into one block."""
    combined = ""
    for path in sorted(DOCS_DIR.glob("*.md")):
        combined += f"## {path.name}\n\n{path.read_text(encoding='utf-8')}\n\n"
    return combined


def ask(question, docs_text):
    """Send the docs + question to Claude and return the grounded answer."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=500,
        system=SYSTEM_PROMPT + docs_text,
        messages=[{"role": "user", "content": question}],
    )
    return message.content[0].text


if __name__ == "__main__":
    # The question to ask: everything after the script name, or a prompt if none given.
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("What's your onboarding question? ")

    docs_text = load_all_docs()
    print(ask(question, docs_text))
