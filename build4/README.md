Build 4 — AI Onboarding Assistant
A command-line assistant that answers new-hire questions using a set of company policy documents. It only answers from the docs it's given, and says "I don't know" when the answer isn't there — instead of guessing. The point is grounding: keeping the AI honest by tying every answer to a source, the way a real internal support bot has to.

Knowledge base: three markdown docs for a fictional company (Meridian Software) — PTO policy, benefits FAQ, and a new-hire onboarding checklist.

Status: done.
- Day 1: folder, docs, and a script that reads a doc. ✅
- Day 2: send the docs to Claude, answer a question grounded in them, refuse when the answer isn't in the docs. ✅

Setup
1. pip install anthropic python-dotenv
2. Create a .env file with your Anthropic API key:
   ANTHROPIC_API_KEY=your_key_here

Run it
Ask a question and it answers using all three docs, or says it doesn't know:

python support_assistant.py What is the PTO policy?

Leave off the question and it'll prompt you for one instead.

What I took away
- Grounding lives in the system prompt, not the user message — that's what makes the "only answer from these docs, otherwise say I don't know" instruction stick.
- Had to stop and relearn functions (`def`, `return`, loop-and-accumulate, `if`/`else`) before this script made sense — Week 1 covered it, but it hadn't actually stuck until I drilled it with fresh examples.
