# pi-gpio
Examples of using Raspberry Pi GPIO libraries on balenaOS. The four libraries demonstrated here have been updated by their maintainers to work across all Raspberry Pi models and current kernel versions without modification. (As Raspberry Pi models have evolved over the years, the hardware driving these GPIO pins has changed multiple times, and not all libraries have kept up with these changes.)

For more information about GPIO on Raspberry Pi see:

- [balenaOS GPIO documentation](https://docs.balena.io/learn/develop/hardware/gpio/#raspberry-pi)
- [Raspberry Pi informative pdf on the history of Pi GPIO](https://pip.raspberrypi.com/categories/685-whitepapers-app-notes/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices.pdf)
- [Example projects](https://projects.raspberrypi.org/en/projects/physical-computing/0) from Raspberry Pi using GPIO. (NOT balena or container-specific)

## GPIO Libraries

Each example library is in a separate folder and will run in a separate container if pushed to a balena device or another container runtime. The libraries do not auto start, since if they did, they would interfere with each other. In other words, only use one of these libraries at a time! (If you get a 'GPIO busy' error, you may need to reboot your Pi.) See the headings below for details on how to run each example library. These examples assume you have connected an LED to GPIO (not pin number) 26. You should probably use a 100 - 330 ohm resister in line with your LED. See the project link above for more details about connecting an LED. The examples will still run without a connected LED, but you won't have any visual feedback that the GPIO is working.

### libgpiod
[libgpiod](https://libgpiod.readthedocs.io/en/latest/) is a C library and set of tools for interacting with the Linux GPIO character devices (/dev/gpiochipX). To run this example, ssh into the `libgpiod` service and run `./example.sh`

### pinctrl
[pinctrl](https://github.com/raspberrypi/utils/tree/master/pinctrl) is a more powerful replacement for raspi-gpio, a tool for displaying and modifying the GPIO and pin muxing state of a system. It accesses the hardware directly, bypassing the kernel drivers. To run this example, ssh into the `pinctrl` service and run `./example.sh`

### rpi-lgpio
[rpi-lgpio](https://rpi-lgpio.readthedocs.io/en/release-0.4/) is a compatibility package intended to provide compatibility with the rpi-gpio (aka RPi.GPIO) library, on top of kernels that only support the gpiochip device (and which have removed the deprecated sysfs GPIO interface). To run this example, ssh into the `rpi-lgpio` service and run `python3 example.py`

### gpiozero
[gpiozero](https://gpiozero.readthedocs.io/en/stable/) is a Python library providing a simple-to-use interface to Raspberry Pi GPIOs. To run this example, ssh into the `gpiozero` service and run `python3 example.py`. Note that as of this writing, gpiozero has some compatibility issues with Pi 5 GPIO, so the example uses a "hack" to ensure compatibility: The patch forces GPIO Zero to use chip 0 on RPi5 and resolves lgpio pin factory issues. See https://github.com/gpiozero/gpiozero/issues/1166#issuecomment-2306937929 for more information.

## Compatibility

Versions of these libraries used for testing:

lgpio Version: 0.2.2.0

gpiozero Version: 2.0.1

gpiod Version: 1.6.3-1+b3

rpi-lgpio Version: 0.6

All libraries tested to work with the results as follows:

| device type | balenaOS version    | kernel version | pinctrl | gpiozero | gpiod | rpi-lgpio |
| ----------- |-------------------- | -------------- |---------|----------|-------|-----------|
| Pi 4        | 6.5.1+rev4          | ?              |
| Pi 5        | 6.5.1+rev5          | 6.12.20        | yes     | yes      | yes   | yes       |
| Pi 5        | 6.5.9               | 6.12.20        | yes     | yes      | yes   | yes       |
| Pi 5        | 5.3.22              | 6.6.22         | yes     | no       | no    | yes       |





