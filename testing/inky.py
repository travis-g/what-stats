"""Testing library to allow for standard debugging with PIL/Pillow"""
from PIL import Image, ImageDraw

WHITE = 0
BLACK = 1
RED = 2
YELLOW = 2

class InkyWHAT:
    """Fallback eInk Display Driver for the InkyWHAT"""
    def __init__(self, colour='red'):
        self.WHITE = '#fff'
        self.BLACK = '#000'
        self.RED = '#f00'
        self.YELLOW = 2
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
