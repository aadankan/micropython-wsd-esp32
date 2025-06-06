from machine import Pin
import neopixel

class RGBLed:
    """
    A class to control RGB LEDs using the NeoPixel library.
    """

    def __init__(self, pin: int, num_leds: int = 1):
        """
        Initializes the RGB LED controller.

        Parameters:
            pin (int): The GPIO pin number to which the LED strip is connected.
            num_leds (int): The number of LEDs in the strip. Default is 1.
        """
        self.pin = Pin(pin, Pin.OUT)
        self.num_leds = num_leds
        self.np = neopixel.NeoPixel(self.pin, self.num_leds)

    def set_color(self, r: int, g: int, b: int):
        """
        Sets the color of all LEDs in the strip.

        Parameters:
            r (int): The red component of the color (0-255).
            g (int): The green component of the color (0-255).
            b (int): The blue component of the color (0-255).
        """
        for i in range(self.num_leds):
            self.np[i] = (r, g, b)
        self.np.write()

    def set_brightness(self, brightness: float):
        """
        Adjusts the brightness of all LEDs in the strip.

        Parameters:
            brightness (float): The brightness level (0.0 to 1.0).

        Raises:
            ValueError: If the brightness is not between 0.0 and 1.0.
        """
        if 0.0 <= brightness <= 1.0:
            for i in range(self.num_leds):
                r, g, b = self.np[i]
                self.np[i] = (int(r * brightness), int(g * brightness), int(b * brightness))
            self.np.write()
        else:
            raise ValueError("Brightness must be between 0.0 and 1.0")

    def rainbow(self, delay: float):
        """
        Displays a rainbow animation on the LED strip.

        Parameters:
            delay (float): The delay between frames in seconds.
        """
        import time
        for j in range(256):
            for i in range(self.num_leds):
                pixel_index = (i * 256 // self.num_leds) + j
                self.np[i] = self.wheel(pixel_index & 255)
            self.np.write()
            time.sleep(delay)

    def wheel(self, pos: int):
        """
        Generates a color based on a position value.

        Parameters:
            pos (int): The position value (0-255).

        Returns:
            tuple: A tuple representing the RGB color (r, g, b).
        """
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)

    def clear(self):
        """
        Turns off all LEDs in the strip by setting their color to black.
        """
        for i in range(self.num_leds):
            self.np[i] = (0, 0, 0)
        self.np.write()