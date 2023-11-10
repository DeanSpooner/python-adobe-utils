# To run, in your terminal run `python3 underscore.py`
# This will replace all spaces with underscores in file names in the current folder, and all subfolders.
import os

def rename_files_with_spaces(starting_directory='.'):
    for root, _, files in os.walk(starting_directory):
        for filename in files:
            if ' ' in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace(' ', '_')
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

# You can specify a different starting directory if needed, e.g., rename_files_with_spaces('/path/to/your/directory')
rename_files_with_spaces()