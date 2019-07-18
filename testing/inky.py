"""Testing library to allow for standard debugging with PIL/Pillow"""
from PIL import Image, ImageDraw

WHITE = '#fff'
BLACK = '#000'
RED = '#f00'
YELLOW = '#ff0'

class InkyWHAT:
    """Fallback eInk Display Driver for the InkyWHAT"""
    def __init__(self, colour='red'):
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.RED = RED
        self.YELLOW = YELLOW
        self.WIDTH = 400
        self.HEIGHT = 300
        self.image = Image.new("P", (self.WIDTH, self.HEIGHT))
    def show(self, busy_wait=True):
        self.image.show()
    def set_image(self, image):
        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

        self.image = image.convert("RGB").quantize(palette=pal_img)
    def set_border(self, colour):
        # TODO
        return
