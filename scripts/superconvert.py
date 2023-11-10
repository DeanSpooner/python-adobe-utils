# To run, in your terminal run `python3 superconvert.py` - this will replace all spaces in file names with underscores,
# convert all .ai files to .svg, then delete all .ai files and this superconvert.py file.
# ENSURE YOU HAVE A COPY OF ALL FILES REQUIRED STORED SAFELY ELSEWHERE BEFORE RUNNING!
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


def convert_ai_to_svg(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.ai') and ' ' not in filename:
                ai_file_path = os.path.join(root, filename)
                name, _ = os.path.splitext(ai_file_path)
                svg_file_path = name + '.svg'
                os.system(
                    f"inkscape {ai_file_path} --export-area-drawing --export-plain-svg={svg_file_path}")
                print(f'Converted: {ai_file_path} -> {svg_file_path}')


def delete_files_recursively(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if os.path.splitext(filename)[1] == '.ai':
                ai_file_path = os.path.join(root, filename)
                print('Deleting', ai_file_path)
                os.remove(ai_file_path)

    # Delete this 'superconvert.py' file in the starting directory
    superconvert_py_path = os.path.join(directory, 'superconvert.py')
    if os.path.exists(superconvert_py_path):
        print('Deleting', superconvert_py_path)
        os.remove(superconvert_py_path)


rename_files_with_spaces()
convert_ai_to_svg()
delete_files_recursively()
