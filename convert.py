# To run, in your terminal run `python3 convert.py` - this will convert all .ai files to .svg and save the SVGs
# into a 'converted' folder.
# Names of files must have no spaces in them, otherwise conversion will fail.
import os

directory = '.'
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.name)
        name = os.path.splitext(filename)[0]
        os.system(
            "inkscape {} --export-area-drawing --export-plain-svg=converted/{}.svg".format(filename.name, name))
