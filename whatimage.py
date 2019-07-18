#!/usr/bin/env python

import imgkit
import argparse
import requests
import os
import subprocess
from font_gohu_font import GohufontUni14
from StringIO import StringIO
try:
    from inky import InkyWHAT
    _image_mode = "P"
except ImportError:
    from testing import InkyWHAT
    _image_mode = "RGB"
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

font = ImageFont.truetype(GohufontUni14, 14)

fulltext = subprocess.check_output(['bar-usage'])
fulltext = fulltext.decode('utf-8')

img = Image.new(_image_mode, (inky_display.WIDTH, inky_display.HEIGHT), inky_display.WHITE)
draw = ImageDraw.Draw(img)

draw.multiline_text((0, 0), fulltext, fill=inky_display.BLACK,
                    font=font, align="left")

inky_display.set_image(img)
inky_display.show()
