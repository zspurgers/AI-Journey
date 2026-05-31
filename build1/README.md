# Build 1 — File Sorter

A Python script that scans a folder and sorts every file into a subfolder named after its extension (e.g. `PDF_Files/`, `JPG_Files/`). Files with no extension go into `NO EXTENSION_Files/`. If a filename already exists at the destination, the script appends a counter (`report_1.pdf`, `report_2.pdf`) instead of overwriting.

## Run it

```
python build1.py <folder_path>
```

Example:

```
python build1.py "C:\Users\zacha\Documents\Messy Folder"
```

## What I took away

- `pathlib.Path` is much cleaner than string-based path handling — `item.stem`, `item.suffix`, and the `/` operator make file logic readable.
- Always check for existing files before renaming. The first version of this script silently overwrote duplicates; the counter loop fixes that.
- Guarding with `folder_path.exists() and folder_path.is_dir()` up front beats letting the script fail mid-run.
