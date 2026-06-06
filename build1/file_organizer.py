import sys #imports the sys library so the script can access command line arguments

from pathlib import Path #imports the Path library to work with file paths

if len(sys.argv) < 2: #checks if the length of the command line arguments is less than 2 (the first argument is the script name)
    print("You are missing the folder path. Please enter it here") 
    folder_path = Path(input()) #takes the above input from the user and converts it to a Path object
    
else:
    folder_path = Path(sys.argv[1]) #takes the second command line argument (the folder path) and converts it to a Path object

if not folder_path.exists(): #checks if the folder path exists. If it doesn't, it prints an error message.
    print("This folder path does not exist") 

elif not folder_path.is_dir(): #checks if the folder path is a directory. If it isn't, it prints an error message.
    print("The filepath is not a directory")
    
else:
    all_items = list(folder_path.iterdir()) #creates a list of all items in the folder

    for item in all_items: #loops through each item in the folder
        if item.is_dir(): #checks if the item is a directory/folder
            continue #skips directories and only prints files

        suffix_text = item.suffix.upper().replace(".", "") #gets the file extension, converts it to uppercase, and removes the dot
        current_type = suffix_text if suffix_text else "NO EXTENSION" #if there is no extension, it will say "NO EXTENSION"

        destination_folder = folder_path / f"{current_type}_Files" #creates a new folder path based on the file type
        destination_folder.mkdir(exist_ok=True) #creates the new folder if it doesn't already exist
        new_file_path = destination_folder / item.name #creates the new file path in the new folder
  
        counter = 1 #initializes a counter to keep track of duplicate file names
        # item.stem gets the name without the extension,  (e.g. "report")
        # item.suffix gets the extension with the dot (e.g. ".pdf")
        while new_file_path.exists(): #loops until it finds a unique file name
            new_file_path = destination_folder / f"{item.stem}_{counter}{item.suffix}" #creates a new file name with the counter (e.g. "report_1.pdf")
            counter += 1 #increments the counter for the next iteration if needed
      
        item.rename(new_file_path) #moves the file to the new folder
        
        print(f"📄 Moved: {item.name} ➡️  {new_file_path.name}")
