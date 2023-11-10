# To run, in your terminal run `python3 deleter.py`
# This will delete all .ai files in the current directory.
# ENSURE YOU HAVE A COPY OF ALL FILES REQUIRED STORED SAFELY ELSEWHERE BEFORE RUNNING!
import os

directory = '.'
for filename in os.scandir(directory):
    if os.path.splitext(filename.name)[1] == '.ai':
        print('Deleting', filename.name)
        os.system(
            "rm {}".format(filename.name))
