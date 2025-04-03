from gpiozero import LED
import time
import gpiozero.pins.lgpio
import lgpio

print("Python gpiozero example...")
print("Blinking LED on GPIO 26 for 5 seconds")

# This "patch" forces GPIO Zero to use chip 0 on RPi5 and resolves lgpio pin factory issues.
# See https://github.com/gpiozero/gpiozero/issues/1166#issuecomment-2306937929
def __patched_init(self, chip=None):
    gpiozero.pins.lgpio.LGPIOFactory.__bases__[0].__init__(self)
    chip = 0
    self._handle = lgpio.gpiochip_open(chip)
    self._chip = chip
    self.pin_class = gpiozero.pins.lgpio.LGPIOPin

gpiozero.pins.lgpio.LGPIOFactory.__init__ = __patched_init

led = LED(26)

led.blink()

time.sleep(5)
