import os
import shutil
import re

def organize_jpg_files(source_dir, target_dir):
    """
    Finds all .jpg/.jpeg files in the source directory and moves them to the target directory.
    """
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return

    # Create the target directory if it doesn't exist yet
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created target directory: {target_dir}")

    # Compile a regular expression to match .jpg, .jpeg, .JPG, and .JPEG
    jpg_pattern = re.compile(r'\.jpe?g$', re.IGNORECASE)
    
    # Counter for moved files
    moved_count = 0

    # Iterate through all items in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Make sure we are only looking at files, not subfolders
        if os.path.isfile(source_path):
            # Use regex to check if the file extension matches
            if jpg_pattern.search(filename):
                target_path = os.path.join(target_dir, filename)
                
                try:
                    # Move the file
                    shutil.move(source_path, target_path)
                    print(f"Moved: {filename} -> {target_dir}")
                    moved_count += 1
                except Exception as e:
                    print(f"Failed to move {filename}. Error: {e}")

    print("---")
    print(f"Task completed! Total files moved: {moved_count}")

# --- Execution Block ---
if __name__ == "__main__":
    # Replace these paths with actual paths on your computer
    # Use absolute paths to avoid any confusion
    SOURCE_FOLDER = r"./Downloads"  # Example: your messy downloads folder
    TARGET_FOLDER = r"./Organized_Photos"  # Example: where you want them to go

    organize_jpg_files(SOURCE_FOLDER, TARGET_FOLDER)