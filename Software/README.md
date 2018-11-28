[![Build Status](https://travis-ci.com/Wright4TheJob/PiKwonDo.svg?branch=master)](https://travis-ci.com/Wright4TheJob/PiKwonDo)
[![codecov](https://codecov.io/gh/Wright4TheJob/PiKwonDo/branch/master/graph/badge.svg)](https://codecov.io/gh/Wright4TheJob/PiKwonDo)
# Software
The PiKwonDo software uses two primary processing threads to control 1) game logic and GUI and 2) scanning buttons and driving GPIO data flow. Software is written in Python and uses PiQT5 for GUI elements.

# Dependencies
* PyQT5
* GPIO

# Installation
Delete the RPi folder in Software to direct the python installtion to the global GPIO library present on the Raspberry Pi. If testing or modifying the software on a desktop computer, the RPi folder mimics the GPIO library and allows the software to run.

# Startup
To start the PiKwonDo software, navigate to the Software folder in the terminal and launch the PyKwonDo.py file using Python 3:
```
$ python3 PyKwonDo.py
```

# Status
Initial software class structure and functionality are in place. Interpretation of the button states is currently rudimentary. GUI is functional.

# Documentation
All documentation is generated using Sphinx and deployed on GihubPages [here]( https://wright4thejob.github.io/PiKwonDo/build/html/index.html). New code commits with correct docstrings can update the documentation by running ```$ make html``` from PiKwonDo/Software/docs.

## TODO
* Add check for system parameters to allow non-Raspberry Pi code testing
* Complete GPIO scanning code and test with hardware.
* Unit test combinations of judge signals.
* Create automated installation script.
