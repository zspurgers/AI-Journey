Build 3 — Multi-Document Summarizer
A Python script that reads every .md file in a folder you point it at, summarizes each one individually using the Claude API, and then writes a combined index file with a per-file summary and an overall overview. Point it at any folder of notes or documents and get a fast picture of what's in there without opening every file.

Real use case: point it at a folder of training material, project notes, or work docs and get a quick index of what each file covers — so you know where to look when you need something, and nothing that needs action gets forgotten.

Setup
1. pip install anthropic python-dotenv
2. Create a .env file with your Anthropic API key:
   ANTHROPIC_API_KEY=your_key_here
3. Create a folder of .md files you want summarized

Run it
Pass the folder path as a command-line argument:

python multi_doc_summarizer.py "C:\path\to\your\folder"

If you forget the path, the script will prompt you to enter one.

Output
The script writes an index.md file in the same directory you run it from. Each source file gets a section with its filename as a header and a bullet-point summary of what it contains. The file closes with a combined overview of everything in the folder.

Example output (index.md):
## budget-tracker.md
A personal script that reads bank CSV exports, auto-categorizes transactions by keyword rules, and totals monthly spending by category. Currently handles ~80% of transactions automatically; considering Claude for the fuzzy 20%.

## file-organizer-bot.md
Automation tool that sorts the Downloads folder into subfolders by file type. Handles duplicate filenames safely. Complete and running on a schedule.

## meeting-notes-agent.md
Records and transcribes meetings, uses Claude to extract action items and decisions. Paused — transcription works but not yet connected to Claude. Needs chunking solution for long transcripts.

Overall summary: All three are personal automation projects. Two are planning to use Claude to handle complex or ambiguous cases that simple rules can't cover.

What I took away
- This was the first build that felt connected to real day-to-day use — something I could actually run at work or at home to save time
- Learned how to loop through files in a folder using pathlib.glob() instead of hardcoding a filename
- Learned the difference between a list variable (.append()) and a file object (.write()) and when to use each
- Learned that opening a file in "w" mode overwrites it on every run — which is actually what you want for a regenerating index
- Learned that sys.argv lets you pass arguments from the command line so the script isn't hardcoded to one folder
- This feels like the beginning of an AI assistant — read a folder, understand what's in it, surface what matters
