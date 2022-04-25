import time

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import sys

from Display.OledDisplay.OledDisplay import OledDisplay

if __name__ == "__main__":
    # Define the Reset Pin
    oled = OledDisplay(2)

    # Clear display.
    oled.fill(0)

    # Make sure to create image with mode '1' for 1-bit color.
    image_name = sys.argv[1]
    image = Image.open(image_name).convert("1")

    # Display image
    oled.show(image)

    time.sleep(30)
