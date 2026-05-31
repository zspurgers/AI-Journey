import sys
from pathlib import Path #importing the Path library to work with file paths

if len(sys.argv) < 2:
    print("Usage: python file_sorter.py <folder_path>")
    sys.exit(1)

folder_path = Path(sys.argv[1]) #specifies the path to the folder we want to work with

if folder_path.exists() and folder_path.is_dir(): #checks if the path exists and is a directory/folder

    all_items = list(folder_path.iterdir()) #creates a list of all items in the folder

    for item in all_items:
        if item.is_dir(): #checks if the item is a directory/folder
            continue #skips directories and only prints files

        suffix_text = item.suffix.upper().replace(".", "") #gets the file extension, converts it to uppercase, and removes the dot
        current_type = suffix_text if suffix_text else "NO EXTENSION" #if there is no extension, it will say "NO EXTENSION"

        destination_folder = folder_path / ( f"{current_type}_Files" ) #creates a new folder path based on the file type
        destination_folder.mkdir(exist_ok=True) #creates the new folder if it doesn't already exist
        new_file_path = destination_folder / item.name #creates the new file path in the new folder
        if new_file_path.exists():
            counter = 1 #initializes a counter to keep track of duplicate file names
            # item.stem gets the name without the extension,  (e.g. "report")
            # item.suffix gets the extension with the dot (e.g. ".pdf")
            while new_file_path.exists(): #loops until it finds a unique file name
                new_file_path = destination_folder / f"{item.stem}_{counter}{item.suffix}" #creates a new file name with the counter (e.g. "report_1.pdf")
                counter += 1 #increments the counter for the next iteration if needed
        item.rename(new_file_path) #moves the file to the new folder
        print(f"📄 Moved: {item.name} ➡️  {new_file_path.name}")

else:
    print("\nThe folder does not exist or is not a directory.\n") #prints a message if the folder does not exist or is not a directory