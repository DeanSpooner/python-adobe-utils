# To run, in your terminal run `python3 deleter_subfolders.py` - this will delete all .ai files.
# This will then delete the convert.py file, and lastly delete this very file - keep a backup of your Python files!

import os

def delete_files_recursively(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if os.path.splitext(filename)[1] == '.ai':
                ai_file_path = os.path.join(root, filename)
                print('Deleting', ai_file_path)
                os.remove(ai_file_path)

    # Delete the 'underscore.py' file in the starting directory
    underscore_py_path = os.path.join(directory, 'underscore.py')
    if os.path.exists(underscore_py_path):
        print('Deleting', underscore_py_path)
        os.remove(underscore_py_path)
    
    # Delete the 'convert.py' file in the starting directory
    convert_py_path = os.path.join(directory, 'convert.py')
    if os.path.exists(convert_py_path):
        print('Deleting', convert_py_path)
        os.remove(convert_py_path)

    # Delete the 'deleter.py' file in the starting directory
    deleter_py_path = os.path.join(directory, 'deleter_subfolders.py')
    if os.path.exists(deleter_py_path):
        print('Deleting', deleter_py_path)
        os.remove(deleter_py_path)

# You can specify a different starting directory if needed, e.g., delete_files_recursively('/path/to/your/directory')
delete_files_recursively()