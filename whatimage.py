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
    from testing import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

font = ImageFont.truetype(Gohufont, 14)

fulltext = subprocess.check_output(['bar-usage'])
fulltext = fulltext.decode('utf-8')

img = Image.new("RGB", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.WHITE)
draw = ImageDraw.Draw(img)

draw.multiline_text((0, 0), fulltext, fill=inky_display.BLACK,
                    font=font, align="left")

inky_display.set_image(img)
inky_display.show()
