import os
import shutil
from pathlib import Path

# Directory to watch (e.g., Downloads folder)
watch_dir = Path('path/to/your/downloads/folder')  # change this path

# Directory where files will be moved to
organized_dir = Path('path/to/your/organized/folder')  # change this path

# File extensions to classify and corresponding folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java'],
}

def create_folders():
    """Create folder structure if it doesn't exist."""
    for folder in file_types.keys():
        folder_path = organized_dir / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)

def organize_files():
    """Organize files in the download folder based on file types."""
    # Create directories if they don't exist
    create_folders()
    
    # Loop through files in the watch directory
    for file in watch_dir.iterdir():
        if file.is_file():
            file_extension = file.suffix.lower()
            moved = False
            
            # Check file extension and move to the corresponding folder
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = organized_dir / folder
                    shutil.move(str(file), target_folder / file.name)
                    print(f"Moved: {file.name} -> {folder}")
                    moved = True
                    break
            
            # If file doesn't match any extension, move it to 'Others'
            if not moved:
                others_folder = organized_dir / 'Others'
                if not others_folder.exists():
                    others_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file), others_folder / file.name)
                print(f"Moved: {file.name} -> Others")

if __name__ == '__main__':
    organize_files()
