#!/usr/bin/env python

import imgkit
import argparse
import requests
import os
import subprocess
from font_gohu_font import Gohufont
from StringIO import StringIO
try:
    from inky import InkyWHAT
except ImportError:
    class inky_display:
        WIDTH = 400
        HEIGHT = 300
        BLACK = 0
        RED = 2
from PIL import Image, ImageFont, ImageDraw

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

font = ImageFont.truetype(Gohufont, 28)

fulltext = 'temp: {}'.format(measure_temp())
fulltext += '\n'
fulltext += subprocess.check_output(['12-usage'])
fulltext = fulltext.decode('utf-8')

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

draw.multiline_text((0, 0), fulltext, fill=inky_display.BLACK,
                    font=font, align="left")

inky_display.set_image(img)
inky_display.show()

# parser = argparse.ArgumentParser()
# parser.add_argument('--image', '-i', type=str, required=True,
#                     help="Input image to be converted/displayed")
# args = parser.parse_args()

# img_file = args.image

# Set up the inky wHAT display and border colour

# Open our image file that was passed in from the command line
# r = requests.get(img_file)
# img = Image.open(StringIO(r.content))

# # Get the width and height of the image
# w, h = img.size

# orientation = "portrait" if h > w else "landscape"

# # if a portrait, rotate for best fit
# if orientation == "portrait":
#     img = img.transpose(Image.ROTATE_270)
#     w, h = img.size

# # Calculate the new height and width of the image

# h_new = 300
# w_new = int((float(w) / h) * h_new)
# w_cropped = 400

# # Resize the image with high-quality resampling

# img = img.resize((w_new, h_new), resample=Image.LANCZOS)

# # Calculate coordinates to crop image to 400 pixels wide

# x0 = (w_new - w_cropped) / 2
# x1 = x0 + w_cropped
# y0 = 0
# y1 = h_new

# # Crop image

# img = img.crop((x0, y0, x1, y1))

# # Convert the image to use a white / black / red colour palette

# pal_img = Image.new("P", (1, 1))
# pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

# img = img.convert("RGB").quantize(palette=pal_img)

# # Display the final image on Inky wHAT
# #inky_display = InkyWHAT("red")
# # inky_display.set_border(inky_display.WHITE)

# # inky_display.set_image(img)
# # inky_display.show()

# # options = {'width': 400, 'height': 300, 'disable-smart-width': ''}
# # img = Image.open(StringIO(imgkit.from_file('./output.html', False)))

# # img.show()
