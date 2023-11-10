# To run, in your terminal run `python3 deleter.py` - this will delete all .ai files in the current directory.
import os

directory = '.'
for filename in os.scandir(directory):
    if os.path.splitext(filename.name)[1] == '.ai':
        print('Deleting', filename.name)
        os.system(
            "rm {}".format(filename.name))
