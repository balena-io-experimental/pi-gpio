import RPi.GPIO as GPIO
import time

print("Running rpi-lgpio example, flashing LED on GPIO 26")

def button_press(channel):
    print("Press: {}".format(channel))
    if channel == 19:
        print("RPi info: model:{}; RAM:{}".format(GPIO.RPI_INFO["TYPE"], GPIO.RPI_INFO["RAM"]))

DEBOUNCE = 500

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(19, GPIO.RISING, callback=button_press, bouncetime=DEBOUNCE)

while True:
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.5)
