import os

def convert_ai_to_svg(directory='.'):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.ai') and ' ' not in filename:
                ai_file_path = os.path.join(root, filename)
                name, _ = os.path.splitext(ai_file_path)
                svg_file_path = name + '.svg'
                os.system(f"inkscape {ai_file_path} --export-area-drawing --export-plain-svg={svg_file_path}")
                print(f'Converted: {ai_file_path} -> {svg_file_path}')

# You can specify a different starting directory if needed, e.g., convert_ai_to_svg('/path/to/your/directory')
convert_ai_to_svg()