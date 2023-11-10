# To run, in your terminal run `python3 deleter_subfolders.py`
# This will delete all .ai files in the current directory and in any subfolders.
# This will then delete any Python files, including this very file.
# ENSURE YOU HAVE A COPY OF ALL FILES REQUIRED STORED SAFELY ELSEWHERE BEFORE RUNNING!
import os

def delete_files_recursively(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if os.path.splitext(filename)[1] == '.ai':
                ai_file_path = os.path.join(root, filename)
                print('Deleting', ai_file_path)
                os.remove(ai_file_path)

    # Delete all python files
        for root, _, files in os.walk(directory):
            for filename in files:
                if os.path.splitext(filename)[1] == '.py':
                    py_file_path = os.path.join(root, filename)
                    print('Deleting', py_file_path)
                    os.remove(py_file_path)

# You can specify a different starting directory if needed, e.g., delete_files_recursively('/path/to/your/directory')
delete_files_recursively()