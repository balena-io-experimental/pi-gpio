echo "pinctl GPIO example script"
echo "Blinking LED on GPIO 26 for 5 seconds."

pinctrl 26 op dh

sleep 1

pinctrl 26 op dl

sleep 1

pinctrl 26 op dh

sleep 1

pinctrl 26 op dl

sleep 1

pinctrl 26 op dh

sleep 1

pinctrl 26 op dl
