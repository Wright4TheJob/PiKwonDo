# Software
The PiKwonDo software uses two primary processing threads to control 1) game logic and GUI and 2) scanning buttons and driving GPIO data flow. Software is written in Python and uses PiQT5 for GUI elements.

# Dependencies
* PyQT5
* GPIO

# Installation
Delete the RPi folder in Software to direct the python installtion to the global GPIO library present on the Raspberry Pi. If testing or modifying the software on a desktop computer, the RPi folder mimics the GPIO library and allows the software to run.

# Status
Initial software class structure and functionality are in place. Interpretation of the button states is currently rudimentary. GUI is functional.

## TODO
* Test GPIO scanning with hardware.
* Unit test combinations of judge signals.
* Create automated installation script.
