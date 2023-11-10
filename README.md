# Adobe Illustrator / Inkscape Python scripts, by [Dean Spooner](https://github.com/DeanSpooner) 🎨 🖌️
Welcome to the Adobe Illustrator / Inkscape Python scripts repository by Dean Spooner. The aim of this repo is to provide a set of useful scripts to help quickly convert Adobe Illustrator .ai files to .svg Scalable Vector Graphics files, using Inkscape CLI and Python.

## Requirements:

- Terminal/command line interface;
- [Python](https://www.python.org/downloads/);
- [Inkscape CLI](https://inkscape.org/doc/inkscape-man.html).

## Usage:
Within this repository is a `scripts` folder, that house different utility functions you can use with you Adobe Illustrator .ai files.

Simply place the script you want to use in the folder or root of where your .ai files sit, open this folder in your terminal, and run
`python3 --NAME OF PYTHON SCRIPT--.py`.

## Scripts:
### convert.py
`python3 convert.py`

This script will simply convert any .ai files to .svg files in the current directory, and save the new SVG files into a new 'converted' folder.

Warning: Any .ai files with spaces in their names will not convert.

### convert_wo_subfolder.py
`python3 convert_wo_subfolder.py`

This script will simply convert any .ai files to .svg files in the current directory, and save the new SVG files into the current folder.

Warning: Any .ai files with spaces in their names will not convert.

### convert_wo_subfolder.py
`python3 convert_in_subfolders.py`

This script will convert any .ai files to .svg files in the current directory as well as any within any subfolders, and save the new SVG files into the same folder as its .ai file source.

Warning: Any .ai files with spaces in their names will not convert.

### deleter.py
`python3 deleter.py`

This script will simply delete any .ai files that exist in the current directory.

### deleter_subfolders.py
`python3 deleter_subfolders.py`

This script will delete any .ai files that exist in the current directory, and that exist in any subfolders. This will then also delete any Python files in the current directory and within any subfolders too, including this Python file itself.

### underscore.py
`python3 underscore.py`

This script will scan through all files in the current directory, and any subfolders, and replace any spaces with underscores in any file names.

Any .ai files that have spaces in their names will not convert correctly using the converter scripts, so this is required for those files.

### superconvert.py
`python3 superconvert.py`

This is a script that combines the power of the above scripts. This will:
1. Run through every file in the current directory, and all subfolders, and convert any spaces to underscores in any file names;
2. Convert every .ai file to a .svg file in the current directory and all subfolders;
3. Delete every .ai file  in the current directory and all subfolders;
4. Delete the superconvert.py script file itself.

This should mean that all these .ai files should now be converted to SVG files and simply occupy the folders their .ai source files once sat. This is a particularly helpful and powerful script if you have a bank of .ai files in lots of folders and subfolders that all need converting at once.

# 🖌️ [Dean Spooner](https://github.com/DeanSpooner) 🎨
