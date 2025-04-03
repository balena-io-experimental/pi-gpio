echo "libgpiod example..."
echo "Using gpioset to blink LED on GPIO 26 three times."
gpioset gpiochip0 26=1
sleep 1
gpioset gpiochip0 26=0
sleep 1
gpioset gpiochip0 26=1
sleep 1
gpioset gpiochip0 26=0
sleep 1
gpioset gpiochip0 26=1
sleep 1
gpioset gpiochip0 26=0
