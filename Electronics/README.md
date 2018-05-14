# Electronics
The PiKwonDo is made of four different electrical boards bundled into three unique and connected elements: the processing core, the PiKwonDoHAT, the timer control board, and the judge control board.

All circuits and PCBs are modeled in KiCAD. PCBs are minimal complexity necessary. Boards are intended to be single-sided and capable of being milled on a home circuit board router.

# Processing Core
The core processing unit of the PiKwonDo is a Raspberry Pi. The system is being tested on a Raspberry Pi 3B+.

# PiKwonDoHAT
The PiKwonDoHAT board mounts to the Raspberry Pi and provides the GPIO interface to the RJ12 ports and external boxes. This board contains no logic, simply provides an I/O adapter.

# Peripheral Boxes
All the peripheral boxes (timer and judge boxes), use shift registers to store the button states and sequentially report buttons states to the processor when requested. This method reduces the number of data lines to the central processor and de-couples the number of data lines from the number of buttons per peripheral.

An LED is lighted by the shift pin of the shift register and will illuminate whenever the central processor is querying the state of the buttons.

## Timer
The timer control board contains 5 buttons: three to control the round timing (Start, Pause, Reset), and two penalty buttons (Red and Blue). A single shift register is used to output the state of these 5 buttons.

## Judge
The judge box board contains 10 buttons corresponding to point values of 1 through 5 for both red and blue. Two shift registers passing data in series are used to store the values of all 10 buttons.
