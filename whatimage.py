#!/usr/bin/env python

import requests
import subprocess
from font_gohu import GohufontUni14
from StringIO import StringIO
from PIL import Image, ImageFont, ImageDraw

try:
    from inky import InkyWHAT
    _image_mode = "P" # palette-based
except ImportError:
    print("falling back to test library...")
    from testing import InkyWHAT
    _image_mode = "RGB" # full rgb

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

font = ImageFont.truetype(GohufontUni14, 14)

fulltext = subprocess.check_output(['uptime'])
fulltext = fulltext.decode('utf-8')

img = Image.new(_image_mode, (inky_display.WIDTH,
                              inky_display.HEIGHT), inky_display.WHITE)
draw = ImageDraw.Draw(img)

draw.multiline_text((0, 0), fulltext, fill=inky_display.BLACK,
                    font=font, align="left")

inky_display.set_image(img)
inky_display.show()
