import os
import glob
import string_utils

font_directory = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'files')

font_files = {
    # Gohufont11
    # Gohufont14
    # GohufontUni11
    # GohufontUni14
}

for font in list(glob.glob(os.path.join(font_directory, "*.ttf"))):
    font_name = string_utils.snake_case_to_camel(
        os.path.basename(font).replace(".ttf", ""), separator="-")
    font_files[font_name] = font
    globals()[font_name] = font
