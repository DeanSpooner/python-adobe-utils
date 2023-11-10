# To run, in your terminal run `python3 get_width_height.py`
# This will work through the python scripts folder and all subfolders to print each .svg files' 
# file name, width, height, and width/height proportion from its viewBox property.
import os

def get_width_height(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.svg'):
                f = open(os.path.join(root, filename), "r")
                data = f.readlines()
                for line in data:
                    if "viewBox" in line:
                        s = line.replace('"', '')
                        split = s.split()
                        calc = float(split[2]) / float(split[3])
                        print(filename, split[2], split[3], calc)

get_width_height()