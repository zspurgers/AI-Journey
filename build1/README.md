# Build 1 — File Sorter

A Python script that scans a folder and sorts every file into a subfolder named after its extension (e.g. `PDF_Files/`, `JPG_Files/`). Files with no extension go into `NO EXTENSION_Files/`. If a filename already exists at the destination, the script appends a counter (`report_1.pdf`, `report_2.pdf`) instead of overwriting.

## Run it

Provide the folder path as a command-line argument:

```
python build1.py "C:\Users\zacha\Documents\Test_Folder"
```

Example:

```
python build1.py
You are missing the folder path. Please enter it here
C:\Users\zacha\Documents\Test_Folder

```

## What I took away

* `pathlib.Path` is much cleaner than string-based path handling — `item.stem`, `item.suffix`, and the `/` operator make file logic readable.
* Always check for existing files before renaming. The first version of this script silently overwrote duplicates; the counter loop fixes that.
* Combined checks like `if A and B:` work when one error message covers both cases. However, this does not give you the exact reason the script failed. Splitting it into if/elif allows the user to know the true reason for the error.
* When making changes to existing code, the biggest issue I ran into was leaving in existing code that should have been replaced by the update. This would cause errors when testing. I learned to go through each line of code, or at least the affected code to follow the workflow and ensure everything works together.
