from machine import Pin, I2C
from lib import ssd1306  # TODO: change location of this library
import time

class OledDisplay:
    """
    A class to control an OLED display using I2C.
    """

    def __init__(self, sda_pin=21, scl_pin=22, freq=400000, width=128, height=32):
        """
        Initializes the OLED display.

        Parameters:
            sda_pin (int): The GPIO pin number for the I2C data line (SDA). Default is 21.
            scl_pin (int): The GPIO pin number for the I2C clock line (SCL). Default is 22.
            freq (int): The frequency for the I2C communication in Hz. Default is 400,000.
            width (int): The width of the OLED display in pixels. Default is 128.
            height (int): The height of the OLED display in pixels. Default is 32.
        """
        # Initialize I2C and OLED display
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq)
        self.width = width
        self.height = height
        self.display = ssd1306.SSD1306_I2C(width, height, self.i2c)
        self.clear()

    def clear(self):
        """
        Clears the OLED display by filling it with black pixels.
        """
        self.display.fill(0)
        self.display.show()

    def write(self, text, x=0, y=0):
        """
        Displays text on the OLED screen.

        Parameters:
            text (str): The text to display on the screen.
            x (int): The x-coordinate (horizontal position) where the text starts. Default is 0.
            y (int): The y-coordinate (vertical position) where the text starts. Default is 0.
        """
        self.display.text(text, x, y)
        self.display.show()

    def demo(self):
        """
        Runs a simple demo to showcase the OLED display functionality.
        """
        self.clear()
        self.write("Hello, World!", 0, 0)
        time.sleep(2)
        self.clear()
        self.write("Demo Complete!", 0, 10)
        time.sleep(2)