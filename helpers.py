from PIL import Image, ImageDraw
from io import StringIO
import requests


def fetch_image(url):
    """Fetches an image by URL. Image must be converted to a palette mode image with rgb_to_palettes"""
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img


def crop_center_image(img, size):
    """Crops and centers an image to a maximum tuple size (width, height)"""
    w_cropped, h_new = size
    w, h = img.size
    # Calculate the new height and width of the image
    w_new = int((float(w) / h) * h_new)

    # Resize the image with high-quality resampling
    img = img.resize((w_new, h_new), resample=Image.LANCZOS)

    # Calculate coordinates to crop image to 400 pixels wide
    x0 = (w_new - w_cropped) / 2
    x1 = x0 + w_cropped
    y0 = 0
    y1 = h_new

    # Crop image
    img = img.crop((x0, y0, x1, y1))
    return img


def rgb_to_palette(img):
    """Converts an "RGB" mode Image to a "P"/palette mode Image"""
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette(
        (255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
    img = img.convert("RGB").quantize(palette=pal_img)
    return img
